# AI Agents 101 with Crew AI
This repo contains samples from a presentation given to the [Cascade Steam](https://www.meetup.com/cascadesteam/) - Data Engineering Group in Bellingham WA on April 24th, 2024.

The presentation can be viewed: [here](https://docs.google.com/presentation/d/1UzHd_yNuXJSmys2YDVopqXW7gEJ-KxvX1xnxdg46KmU/edit?usp=sharing).

Agent framework: [Crew AI](https://github.com/joaomdmoura/crewAI)

## Running the samples
To run the samples
1. Get the code.
    1. Clone the repo, be sure to have python3 installed.
    2. Or if you have Codespaces enabled on your GitHub acount...
        1. From the project home page click Code (Green button) > Codespaces > +, to create a new codespace
1. Rename `.env.example` to `.env`
1. Edit `.env` and populate it with your `OPENAI_API_KEY` and optionally `LANGCHAIN_API_KEY` (For Langsmith tracing)
1. Run `pip install -r requirements.txt`
1. See the readme.md in each subfolder for the command to run the example.  For each sample, you must navigate to the folder `cd <folder>` before running it.
