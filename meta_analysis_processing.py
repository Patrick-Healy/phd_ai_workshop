import pandas as pd
import json
import concurrent.futures
from tqdm import tqdm

# Task description for generating meta-analysis of academic papers
task_description = (
    "Generate a meta-analysis table for academic papers in economics. "
    "For each paper, extract the following key information:\n"
    "- Paper ID: A unique identifier for the paper (e.g., P001, P002).\n"
    "- Author(s): The authors of the paper.\n"
    "- Year: The publication year of the paper.\n"
    "- Paper Title: The title of the paper.\n"
    "- Journal-Specific ID: The unique identifier for the paper (e.g., DOI, RePEc ID).\n"
    "- Research Question(s) (Quotation): The main research question(s) quoted directly from the paper.\n"
    "- Methodology/Design: A brief description of the methodology or research design.\n"
    "- Key Variables/Concepts: Main variables or concepts explored in the paper. Specify dependent and independant.\n"
    "- Sample/Population: Information about the data/sample (e.g., size, location, time period).\n"
    "- Main Results/Findings: Key results and significant findings.\n"
    "- Effect Size/Impact: A summary of the effect size or impact (e.g., regression coefficients).\n"
    "- Key Statistical Measures: Important statistical measures (e.g., p-values, R-squared).\n"
    "- Data Source: The source of data (e.g., dataset, government sources).\n"
    "- Limitations/Robustness Checks: Summary of limitations or robustness checks.\n"
    "- Implications for Policy/Practice (Quotation): Policy implications quoted from the paper.\n"
    "- Open Questions/Future Research (Quotation): Open questions or suggestions for future research.\n"
    "Additionally, for each paper, evaluate its relevance to the following research question:\n"
    "How does the use of AI-based text mining tools enhance the identification of emerging research trends in academic publications?\n"
    "Provide a Likert scale score (1 to 5) of how relevant the paper is to the research question. "
    "Also, provide a list of reasons why the paper is relevant or not relevant to the research question. and make suggestions of contributions that could be made to open research questions\n"
    "Return the results in the following JSON format:\n"
    "[\n  {\n"
    "    \"paper_id\": \"<paper_id>\",\n"
    "    \"author(s)\": \"<author(s)\",\n"
    "    \"year\": <year>,\n"
    "    \"paper_title\": \"<paper_title>\",\n"
    "    \"journal_specific_id\": \"<journal_specific_id>\",\n"
    "    \"research_question\": \"<research_question>\",\n"
    "    \"methodology\": \"<methodology>\",\n"
    "    \"key_variables\": \"<key_variables>\",\n"
    "    \"sample_population\": \"<sample_population>\",\n"
    "    \"main_results\": \"<main_results>\",\n"
    "    \"effect_size\": \"<effect_size>\",\n"
    "    \"key_statistical_measures\": \"<key_statistical_measures>\",\n"
    "    \"data_source\": \"<data_source>\",\n"
    "    \"limitations\": \"<limitations>\",\n"
    "    \"implications_for_policy\": \"<implications_for_policy>\",\n"
    "    \"open_questions\": \"<open_questions>\",\n"
    "    \"likert_scale\": <likert_scale>,\n"
    "    \"relevance_reasons\": \"<relevance_reasons>\"\n"
    "  }\n]"
)

def process_chunk(chunk, df, client, temperature):
    """
    Process a DataFrame chunk: build the input, call the API,
    parse the JSON response, and return a DataFrame with the results.
    """
    # Extract relevant details from the chunk.
    paper_urls = chunk['Paper URL'].tolist()
    paper_titles = chunk['Title_Abstract'].tolist()
    paper_conclusions = chunk['Conclusion'].tolist()
    
    # Build input text for the chunk with task description and paper details.
    batch_input = "\n\n".join([
        f"Paper URL: {url}\nTitle & Abstract: {title}\nConclusion: {conclusion}"
        for url, title, conclusion in zip(paper_urls, paper_titles, paper_conclusions)
    ])
    input_text = f"{batch_input}\n\nMeta-Analysis Task Details:\n{task_description}"
    
    # Call your GPT API with the temperature setting.
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Adjust model as necessary.
        messages=[
            {"role": "system", "content": "You are an assistant specializing in extracting meta-analysis details from academic papers."},
            {"role": "user", "content": f"{task_description}\n\n{input_text}"}
        ],
        temperature=temperature  # Set the temperature dynamically.
    )
    result_text = response.choices[0].message.content.strip()

    # Remove code block formatting if present.
    if result_text.startswith("```json"):
        result_text = result_text[7:]
    if result_text.endswith("```"):
        result_text = result_text[:-3]
    
    # Parse the JSON response.
    try:
        parsed_data = json.loads(result_text)
        if isinstance(parsed_data, list) and len(parsed_data) == len(paper_urls):
            results = []
            for item in parsed_data:
                # Extract details from the parsed JSON data
                paper_id = item.get('paper_id', 'Unknown')
                author = item.get('author(s)', '')
                year = item.get('year', 'Unknown')
                paper_title = item.get('paper_title', '')
                journal_id = item.get('journal_specific_id', '')
                research_question = item.get('research_question', '')
                methodology = item.get('methodology', '')
                key_variables = item.get('key_variables', '')
                sample_population = item.get('sample_population', '')
                main_results = item.get('main_results', '')
                effect_size = item.get('effect_size', '')
                statistical_measures = item.get('key_statistical_measures', '')
                data_source = item.get('data_source', '')
                limitations = item.get('limitations', '')
                implications_for_policy = item.get('implications_for_policy', '')
                open_questions = item.get('open_questions', '')
                likert_scale = item.get('likert_scale', 'Unknown')  # Default to 'Unknown'
                relevance_reasons = item.get('relevance_reasons', '')  # Default to an empty string
                
                results.append((paper_id, author, year, paper_title, journal_id, research_question, methodology,
                                key_variables, sample_population, main_results, effect_size, statistical_measures,
                                data_source, limitations, implications_for_policy, open_questions, likert_scale, relevance_reasons))
        else:
            # Default values in case the structure doesn't match
            results = [('Unknown', '', 'Unknown', '', '', '', '', '', '', '', '', '', '', '', '', '', '') for _ in paper_urls]
    except json.JSONDecodeError:
        results = [('Unknown', '', 'Unknown', '', '', '', '', "", "", "", "", "", "", "", "", "", "") for _ in paper_urls]
    
    # Create a DataFrame for the results and combine it with the original chunk.
    results_df = pd.DataFrame(results, columns=[
        'Paper_ID', 'Author(s)', 'Year', 'Paper_Title', 'Journal_Specific_ID', 'Research_Question',
        'Methodology', 'Key_Variables', 'Sample_Population', 'Main_Results', 'Effect_Size',
        'Key_Statistical_Measures', 'Data_Source', 'Limitations', 'Implications_for_Policy', 'Open_Questions',
        'Relevance_Likert_Scale', 'Relevance_Reasons'
    ])
    chunk = chunk.reset_index(drop=True)
    combined_df = pd.concat([chunk, results_df], axis=1)
    return combined_df

def process_papers_in_parallel(df, client, chunk_size=1, n_workers=20, temperature=0.7):
    """
    Process papers in parallel using a ThreadPoolExecutor with a progress bar.
    """
    # Split df (your input DataFrame containing papers) into chunks.
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

    # Process each chunk in parallel using ThreadPoolExecutor with a progress bar.
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        results_dfs = list(
            tqdm(
                executor.map(lambda chunk: process_chunk(chunk, df, client, temperature), chunks),
                total=len(chunks),
                desc="Processing chunks in parallel"
            )
        )

    # Concatenate all the chunk DataFrames into one final DataFrame.
    final_df = pd.concat(results_dfs, ignore_index=True)
    return final_df
