// Import necessary modules
import { ChatOpenAI } from "langchain/chat_models/openai";
import { PromptTemplate } from "langchain/prompts";
import { SupabaseVectorStore } from "langchain/vectorstores/supabase";
import { OpenAIEmbeddings } from "langchain/embeddings/openai";
import { StringOutputParser } from "langchain/schema/output_parser";
import { createClient } from "@supabase/supabase-js";

// Define the OpenAI API key
const openAPIkey = process.env.OPEN_API_KEY;

// Initialize a ChatOpenAI instance
const llm = new ChatOpenAI({ openAIApiKey: openAPIkey });

// Define Supabase URL and API key
const supabase_url = "https://vnfifwsblpfforaszzkn.supabase.co";
const supabase_key = process.env.SUPABASE_API_KEY;

// Create a Supabase client
const client = createClient(supabase_url, supabase_key);

// Initialize OpenAIEmbeddings and SupabaseVectorStore instances
const embeddings = new OpenAIEmbeddings({ openAIApiKey: openAPIkey });
const vectorstore = new SupabaseVectorStore(embeddings, {
    client,
    tableName: "documents",
    queryName: "match_documents",
});

// Create a retriever from the vector store
const retriever = vectorstore.asRetriever();

// Define the question
const question = "what is PII and what can aws do protect it?";

// Define a template for generating a standalone question
const standalone_question = "Generate a standalone question based on {question} make as concise as possible \
if the question is a statement get to the core issue and extract a standalone question from it. standalone question:";
const standalone_question_prompt = PromptTemplate.fromTemplate(standalone_question);

// Chain for processing the standalone question
const standalone_question_prompt_chain = await standalone_question_prompt.pipe(llm)
    .pipe(new StringOutputParser())
    .pipe(retriever);

// Invoke the chain to get vectorstore_contexts
const vectorstore_contexts = await standalone_question_prompt_chain.invoke({ question: question });

// Function to combine documents into a single string
function combine_documents(documents) {
    return documents.map((doc) => (doc.pageContent)).join('\n\n');
}

// Define a template for generating the final response
const final_response = "Generate an answer based on the original question {question} and try to find the answer in \
the context using the context {context} if an answer is not present in the context have the user email Elliott @ theCloudShepherd@gmail.com \
always be concise and friendly with your responses. Like you are speaking to a friend. \
answer:";
const final_response_prompt_template = PromptTemplate.fromTemplate(final_response);

// Chain for processing the final response
const final_response_chain = await final_response_prompt_template.pipe(llm);

// Invoke the chain to get the final result
const result = await final_response_chain.invoke({
    question: question,
    context: combine_documents(vectorstore_contexts),
});

// Log the final result to the console
console.log(result);
