import {ChatOpenAi } from "langchain/chat_models/openai"
import {PromptTemplate} from "langchain/prompts"

const openAPIkey = process.env.OPEN_API_KEY;

const llm = ChatOpenAi()