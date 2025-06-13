# Good Prompt / Bon Prompt

## Sources:

-   [Best Practices for Prompt Engineering with OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
-   [Anthropic - Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
-   [Learn Prompting - Introduction](https://learnprompting.org/docs/introduction)
-   [Superhuman's Prompts Cheat Sheet](https://www.superhuman.ai/c/prompts-cheat-sheet)
-   [Lenny's Newsletter - Five Proven Prompt Engineering Techniques](https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques)
-   [GitHub - Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)
-   [Exploding Topics - AI Newsletters](https://explodingtopics.com/blog/ai-newsletters)
-   [Neat Prompts](https://www.neatprompts.com)

# EN

## Summary:

### Why a well-written prompt is essential

OpenAI, Anthropic, and Superhuman all repeat the same idea: AI follows exactly
what you tell it. A clear prompt, separated from its context by triple quotes or
tags, gets much better results than a vague question.

### Basic recipe for a good prompt

-   **Clear purpose** (e.g., "Summarize in 3 bullet points")
-   **Context** (who is the audience, what tone)
-   **Example or output model** (few-shot)
-   **Role** ("You are a marketing expert...")
-   **Steps for complex tasks** ("Reason step by step")

These five building blocks appear in all sources, including Superhuman's cheat
sheet and Lenny's top 5.

### Techniques that work well

-   **Role-play**: asking the AI to take on a character or profession
-   **Few-shot**: providing 2-3 examples before the actual question
-   **Chain-of-thought**: saying "explain your reasoning"
-   **Style unbundling**: the AI first lists traits of a style, then reuses them
-   **Emotion prompting**: reminding the AI of the task's importance to get a
    more careful response

### Staying updated and sharing

Good prompts evolve: newsletters like Ben's Bites or Prompt Engineering Daily
and collaborative repositories (Awesome Prompt Engineering) publish new tricks
and examples every week.

### Tools to go further

-   **xAI's PromptIDE**: a "VS Code" dedicated to prompts, with token-by-token
    analysis
-   **Free guides** (Learn Prompting) provided by Anthropic

## Tips:

-   Start simple: write the need in one sentence, test, then add context and
    format
-   Always separate instructions
-   Provide a response example if you want a specific format
-   Limit length: several small prompts are better than one big block
-   Continuously learn: subscribe to two or three AI newsletters and draw from
    public "prompt libraries"
-   Make it ask questions to better understand the need

## Example:

As part of technology watch, I need a structure to properly create my summaries.
In a continuous improvement framework, you will take on the role of an IT
professor and ask me questions to better understand what my watch is about and
to better structure my outline.

However, I would like to have a format of the following type:

Source: {my sources}

Summary: {my summary}

Tips: {tips I've learned or that I know}

Example: {if I have examples}

[See the complete example](https://chatgpt.com/share/6849ebcb-6f50-8005-8127-65a90fcac57a)

# FR

## Résumé :

### Pourquoi un "prompt" bien écrit est capital

OpenAI, Anthropic et Superhuman répètent la même idée : l'IA suit exactement ce
qu'on lui dit. Un prompt clair, séparé de son contexte par des triples
guillemets ou des balises, obtient de bien meilleurs résultats qu'une question
vague.

### Recette de base pour un bon prompt

-   **But précis** (ex : "Résume-moi en 3 puces")
-   **Contexte** (qui est le public, quel ton)
-   **Exemple ou modèle de sortie** (few-shot)
-   **Rôle** ("Tu es expert marketing…")
-   **Étapes pour les tâches complexes** ("Raisonne étape par étape")

Ces cinq briques reviennent dans toutes les sources, y compris la "cheat-sheet"
de Superhuman et le top 5 de Lenny.

### Techniques qui marchent bien

-   **Role-play** : demander à l'IA d'endosser un personnage ou un métier
-   **Few-shot** : donner 2-3 exemples avant la vraie question
-   **Chain-of-thought** : dire "explique ton raisonnement"
-   **Style unbundling** : l'IA liste d'abord les traits d'un style, puis les
    réemploie
-   **Emotion prompting** : rappeler l'importance de la tâche pour obtenir une
    réponse plus soignée

### Rester à jour et partager

Les bons prompts évoluent : newsletters comme Ben's Bites ou Prompt Engineering
Daily et dépôts collaboratifs (Awesome Prompt Engineering) publient nouveaux
trucs et exemples chaque semaine.

### Outils pour aller plus loin

-   **PromptIDE de xAI** : un "VS Code" dédié aux prompts, avec analyse
    token-par-token
-   **Guides gratuits** (Learn Prompting) fournis par Anthropic

## Les conseils

-   Commencer simple : écrire le besoin en une phrase, tester, puis ajouter
    contexte et format
-   Toujours séparer les instructions
-   Donner un exemple de réponse si l'on veut un format précis
-   Limiter la longueur : mieux vaut plusieurs petits prompts qu'un bloc
    fourre-tout
-   Se former en continu : s'abonner à deux-trois newsletters AI et piocher dans
    les "prompt libraries" publiques
-   Faire en sorte qu'il pose des questions pour mieux comprendre le besoin

## Exemple :

Dans le cadre d'une veille technologique j'ai besoin d'une structure pour bien
faire mes résumés. Dans un cadré d'amélioration continue tu va te positionné en
tant que professeur IT et me poser des question pour mieux comprendre de quoi
parle ma veille et pour mieux structuré ma trame.

J'aimerais cependant avoir une forme de ce type suivant :

Source : {mes sources}

Résumé : {mon résumé}

Les conseils {les conseils que j'en est tiré ou que je connais}

exemple {si j'ai des exemples}

[Voir l'exemple complet](https://chatgpt.com/share/6849ebcb-6f50-8005-8127-65a90fcac57a)
