import asyncio
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os
load_dotenv()
 

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
else:
    print(f"[debug] GEMINI_API_KEY: {gemini_api_key}")

MODEL = "gemini/gemini-2.0-flash"


set_tracing_disabled(disabled=True)

@function_tool
def weather_tool(location:str)->str:
   """
    Returns weather information for a given location.
    """
   print(f"[debug] getting weather for {location}")
   return f"The weather in {location} is sunny."


async def main():
    weather_agent = Agent(
        name= "weather_assistant",
        instructions="You only respond in haikus.and you can use the tool to get the weather.",
        model=LitellmModel(model=MODEL, api_key=gemini_api_key),
        tools=[weather_tool],
        handoff_description="you can respond for weather related queries and you can use the weather tool to get weather info .",
      
    )

    panaversity_agent = Agent(
        name = "panaversity_assistant",
        instructions="you only respond for panaversity related queries",
        model =LitellmModel(model = MODEL, api_key=gemini_api_key),
        handoff_description="you can respond for panaversity related queries",
    )

    main_agent = Agent(
        name = "general_assistant",
        instructions="you are a general assistant and you can use the panaversity agent to get the panaversity related queries and also you can use the weather agent to get the weather information.",
        model = LitellmModel(model=MODEL, api_key=gemini_api_key),
        handoffs=[panaversity_agent,weather_agent]
    )
    result = await Runner.run(main_agent, "hello")
    print(result.final_output)


if __name__ == "__main__": 
    asyncio.run(main())