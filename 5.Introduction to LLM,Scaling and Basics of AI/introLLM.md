## AI, Machine Learning, Deep Learning & LLM — Summary

### 1. Artificial Intelligence (AI)

**AI = Artificial Intelligence**

- Broad field of Computer Science.
- Makes computers perform tasks that normally require human intelligence.
- Examples: reasoning, decision-making, vision, language understanding.

### 2. Machine Learning (ML)

**ML is a subset of AI.**

Instead of explicitly programming every rule, the system learns patterns from data.

**Dataset → Algorithm → Learn Patterns → Prediction**

### 3. Machine Learning Algorithm Types

**Supervised Learning**

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- KNN
- Naive Bayes
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

**Unsupervised Learning**

- K-Means Clustering
- Hierarchical Clustering
- PCA

### 4. Deep Learning (DL)

**Deep Learning is a subset of Machine Learning.**

It uses **Neural Networks with multiple layers** to learn complex patterns from large amounts of data.

**Data → Neural Network → Multiple Layers → Learn Complex Patterns → Prediction**

Input Layer → Hidden Layers → Output Layer
Common Deep Learning types:

- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- LSTM
- GRU
- Transformers

Used for:

- Image recognition
- Speech recognition
- Computer vision
- Natural Language Processing
- Generative AI

mse => mean squared error
mae => mean absolute error = | ypred - yorigin |
in major neural network , major type of operation :
Matrix Multiplication,

Transformer Architecture => A words importance or meaning heavily influenced by its neightbours,
and the context in which we are speaking /saying it.

Attention Mechanism : This mechanism lets the neural network decide the how the other words ,
influence the current word under consideration.

### 5. Large Language Model (LLM)

**LLM = Large Language Model**

LLMs are large AI models trained on huge amounts of text/data to learn patterns in language.

Examples of tasks:

- Text generation
- Question answering
- Translation
- Summarization
- Code generation
- Conversation

### 🧠 Overall Structure

```text
Artificial Intelligence (AI)
│
└── Machine Learning (ML)
    │
    ├── Traditional ML Algorithms
    │   ├── Linear Regression
    │   ├── Decision Tree
    │   ├── Random Forest
    │   ├── KNN
    │   └── ...
    │
    └── Deep Learning (DL)
        │
        ├── ANN
        ├── CNN
        ├── RNN
        ├── LSTM
        ├── GRU
        └── Transformers
              │
              └── Large Language Models (LLMs)
```

### ⭐ Easy way to remember

**AI → ML → Deep Learning → Transformers → LLM**

**AI → ML → Deep Learning → Transformers → LLM**

How LLM actually came up

Pre training => raw internet data
Supervised Fine Tunning
Reinforcement Learning

Web scraper
Seed urls.  
Starting web pages

Web Crawling
Find the html and internal hyperlinks

url filtering

extract text

higher level filtering

Fine Web :decating the web for the finest text data at scale

Similar dataset can be used for training a model

Raw text Convert => Mathematical Representation

Tokenization => Mechanism with which we convert raw text data into a sequence of integer IDS from a given vocalabary.

# Tokens = > Fundamental unit that neural networks can process.

algorithm for creating tokens from text for feeding to LLMS

bite/bytes/token
1.Byte pair encoding BPE
2.Word Piece

# Pre training

Training the neural network :Given a sequence of tokens,predict the probability over what the next token
should be

Output of pre training is called the base model or foundation model

# Post training

# Post-Training

**Goal:** Turn a pretrained model into a useful **AI assistant**.

After pretraining, the model already knows patterns from large amounts of data. **Post-training teaches it how to behave, follow instructions, and respond helpfully.**

### 1. Supervised Fine-Tuning (SFT)

- Train the model using **high-quality conversational/instruction data**.
- Humans provide examples of:
  - User question → Good assistant response
- The model learns how to follow instructions and communicate.

**Example:**

```text
User: Explain AI simply.
Assistant: AI is a field of computer science...
```

### 2. Reward Model (RM)

- A reward model learns **which responses humans prefer**.
- Humans compare multiple model responses and rank/prefer them.
- The reward model learns to give higher scores to better responses.

```text
Response A → Human prefers ✅
Response B → Human doesn't prefer ❌

        ↓

Reward Model learns human preferences
```

### 3. Reinforcement Learning from Human Feedback (RLHF)

**RLHF = Reinforcement Learning from Human Feedback**

- The model generates responses.
- The **Reward Model** evaluates them.
- Reinforcement learning updates the model to produce responses that receive higher rewards.

LLM is a neurral network that runs on top of transformer architecture

Neaural network is a complex mathematical equation
