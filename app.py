from flask import Flask, request, jsonify
from autogpt.commands.command import CommandRegistry, command
from autogpt.prompts.generator import PromptGenerator
from autogpt.app import execute_command, get_command

app = Flask(__name__)

@app.route('/api/command', methods=['POST'])
def process_command():
    try:
        # Check if the request.json object is present.
        if not request.json:
            return jsonify({'error': 'No request.json object present'}), 400

        # Extract the command and arguments from the request.json object.
        command_name = request.json['command_name']
        arguments = request.json['arguments']

        # Execute the command and return the result.
        command_registry = CommandRegistry()
        prompt = PromptGenerator()
        result = execute_command(command_registry, command_name, arguments, prompt)

        return jsonify({'result': result})

    except Exception as e:
        # Return an error message if something goes wrong.
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()