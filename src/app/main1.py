from agents import Agent,Runner, set_default_openai_client, set_tracing_disabled,AsyncOpenAI, set_default_openai_api
import os
from dotenv import load_dotenv
from agents import enable_verbose_stdout_logging
import asyncio

load_dotenv()
enable_verbose_stdout_logging()

gemini_api_key = os.getenv("GEMINI_API_KEY")
print(f"[debug] GEMINI_API_KEY: {gemini_api_key}")


set_tracing_disabled(True)
set_default_openai_api("chat_completions")


external_client =  AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
)

set_default_openai_client(external_client)

async def main()-> None:

    web_agent: Agent = Agent(                             
        name= "web assistant",
        instructions="You are a web assistant and you can only respond for web related queries.",
        model = "gemini-2.0-flash",
        handoff_description="you can respond for web related queries"
    
    )

    mob_agent: Agent = Agent(
        name = "mobile assistant",
        instructions="You are a mobile assistant and you can only  response for mobile related queries.",
        model = "gemini-2.0-flash",
        handoff_description="you can respond for mobile related queries"
    )
    openai_agent: Agent = Agent(
        name = "openai sdk assistant",
        instructions="You are a OpenAI sdk assistant and you can only respond for openai related queries.",
        model = "gemini-2.0-flash",
        handoff_description="you can respond for openai related queries"
    )

    devops_agent: Agent = Agent(
        name = "devops assistant",
        instructions="You are a DevOps assistant and you can only respond for devops related queries.",
        model = "gemini-2.0-flash",
        handoff_description="you can respond for devops related queries"
    )

    agentic_agent: Agent = Agent(
        name = "agentic assistant",
        instructions="You are a Agentic AI assistant and you can only respond for agentic AI queries as well as devops and openai sdk queries using given tools.",
        model = "gemini-2.0-flash",
        handoff_description="you can respond for agentic AI related queries",
        tools=[
            devops_agent.as_tool(
            tool_name="devops_tool",
            tool_description="You can use this tool to get the devops related queries."
            ),
            openai_agent.as_tool(
            tool_name="openai_tool",
            tool_description="You can use this tool to get the openai related queries."
            )
        ]
    )

    panacloud_agent: Agent = Agent(
        name = "general panacloud assistant",
        instructions="You are a general assistant and you can just chat with user and you can use the agentic agent to get the agentic AI related queries and also you can use the web agent to get the web related queries and also you can use mob_agent to get the mobile related quereis.",
        model = "gemini-2.0-flash",
        handoffs=[web_agent,agentic_agent,mob_agent]
    )

    result = await Runner.run(panacloud_agent, "tell me in detail what is  basically  Devops and also openai sdk? ")
    print(result.final_output) 
    print(result.last_agent)

if __name__ == "__main__":
    asyncio.run(main())