from generic_exercise_types import Exercises
from uuid import uuid4

class Rendering:
    
    katex_version = "0.16.22"

    def __init__(self, title: str = '', description: str = '', exercises: Exercises = None):
        self.title = title
        self.description = description
        self.exercises = exercises or []

    def execute(self):
        with open('index.html', 'w') as f:
            f.write(self.render_page())

    @staticmethod
    def render_latex(latex: str) -> str:
        """
        Creates HTML for rendering the given LaTeX code using KaTeX.
        Uses KaTeX for rendering without creating a web component.
        
        :param latex: LaTeX code to render
        :return: HTML string for LaTeX rendering
        """
        # Escape the LaTeX string for JavaScript
        escaped_latex = latex.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
        
        # Create a simple div with KaTeX rendering
        uuid = uuid4()
        html = f"""
    <div class="katex-container" id="{uuid}">
    </div>
    <script>
        katex.render(
            "{escaped_latex}", 
            document.getElementById('{uuid}'), 
            {{ throwOnError: false, displayMode: true }}
        );
    </script>
    """
        return html
        
        
    def render_page(self) -> str:
        """
        Creates a complete HTML5 page string using title, description and exercises.
        
        :return: Complete HTML5 page as a string
        """

        return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{self.title}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{Rendering.katex_version}/dist/katex.min.css">
        <script src="https://cdn.jsdelivr.net/npm/katex@{Rendering.katex_version}/dist/katex.min.js"></script>
        {Rendering.add_styles()}
    </head>
    <body>
        <header>
            <h1>{self.title}</h1>
            <div class="description">{self.description}</div>
        </header>
        
        <main>
            <div class="exercise-container">
            {self.render_exercises()}   
            </div>
        </main>
            
        <footer>
            <p>Generated with KaTeX renderer</p>
        </footer>
    </body>
</html>"""
    

    @staticmethod
    def add_styles():
        return f"""
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        header {{
            margin-bottom: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}
        h1 {{
            color: #2c3e50;
        }}
        .description {{
            color: #7f8c8d;
            font-size: 1.1em;
            margin-bottom: 30px;
        }}
        .exercise-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .exercise {{
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 15px;
            background-color: #f9f9f9;
        }}
        .exercise-content {{
            display: flex;
            flex-direction: row;
            gap: 20px;
            justify-content: space-around;
            align-items: center;
        }}
        .katex-output {{
            margin: 10px 0;
            overflow-x: auto;
        }}
    </style>
"""

    def render_exercises(self):
        exercises = ""
        # Add exercises if available
        for i, exercise in enumerate(self.exercises):
            exercises += f"""
            <div class="exercise" id="exercise-{i + 1}">
                <h3>Aufgabe {i + 1}</h3>
                <div class="exercise-content">
                    {Rendering.render_latex(exercise.question)}
                    {Rendering.render_latex(exercise.answer)}
                </div>
            </div>"""
        return exercises