{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNN8YeDYHE1yhchNqBCUHWF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/centurion027/COP1000-Python/blob/main/module04COP1000_Module04_GuessTheNumber.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "IKMopHnQCahz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "35e34856-cc75-4927-b167-a35695886f25"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to Steven's Guess the Number Program! \n",
            "I am thinking of a number between 1 and 20. \n",
            "What is your guess: 10\n",
            "Your guess is too high\n",
            "Guess again: 5\n",
            "Your guess is too low\n",
            "Guess again: 7\n",
            "Your guess is too high\n",
            "Guess again: 6\n",
            "Correct!\n",
            "You guessed the number in 4 attempts\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "secret_number = random.randint(1, 20)\n",
        "\n",
        "user_number = int(input(\"Welcome to Steven's Guess the Number Program! \\nI am thinking of a number between 1 and 20. \\nWhat is your guess: \"))\n",
        "\n",
        "attempts = 1\n",
        "\n",
        "while secret_number != user_number:\n",
        "  #Too Low\n",
        "  if secret_number > user_number:\n",
        "    print(\"Your guess is too low\")\n",
        "    user_number = int(input(\"Guess again: \"))\n",
        "    attempts += 1\n",
        "  #Too High\n",
        "  else:\n",
        "    print(\"Your guess is too high\")\n",
        "    user_number = int(input(\"Guess again: \"))\n",
        "    attempts += 1\n",
        "#Just Right\n",
        "print(\"Correct!\")\n",
        "print(f\"You guessed the number in {attempts} attempts\")"
      ]
    }
  ]
}
