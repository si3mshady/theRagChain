import { ChatOpenAI } from "langchain/chat_models/openai"
import { PromptTemplate} from "langchain/prompts"

const openAPIkey = process.env.OPEN_API_KEY;

const llm = new ChatOpenAI({openAIApiKey:openAPIkey})

const liTemplate = "Generate a linkedin post based on the following description {description}.\
 Also Generate a title and description for a corresponding youtube video that will capture attention"

const liPrompt =  PromptTemplate.fromTemplate(liTemplate)

// console.log(liPrompt)

const liPromptChain = liPrompt.pipe(llm) 
// 
// console.log(liPromptChain)

const response = await liPromptChain.invoke({
    description: "Foods for brain health"
})

console.log(response.content)