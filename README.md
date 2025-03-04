# LLM Post-Training: A Deep Dive into Reasoning Large Language Models

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)  [![arXiv](https://img.shields.io/badge/arXiv-2502.21321-b31b1b.svg)](https://arxiv.org/pdf/2502.21321)  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/zzli2022/System2-Reasoning-LLM)
[![Contribution Welcome](https://img.shields.io/badge/Contributions-welcome-blue)]()

Welcome to the **Awesome-LLM-Post-training** repository! This repository is a curated collection of the most influential papers, code implementations, benchmarks, and resources related to **Large Language Models (LLMs) Post-Training  Methodologies**. 

Our work is based on the following paper:  
📄 **LLM Post-Training: A Deep Dive into Reasoning Large Language Models** – Available on [![arXiv](https://img.shields.io/badge/arXiv-2502.21321-b31b1b.svg)](https://arxiv.org/pdf/2502.21321)

Authors: **Komal Kumar∗, Tajamul Ashraf∗, Omkar Thawakar, Rao Muhammad Anwer, Hisham Cholakkal, Mubarak Shah, Ming-Hsuan Yang, Phillip H.S. Torr, Fahad Shahbaz Khan, Salman Khan**. 

**📌 Note:**  
- **Corresponding authors:** [Komal Kumar](mailto:komal.kumar@mbzuai.ac.ae), [Tajamul Ashraf](mailto:tajamul.ashraf@mbzuai.ac.ae).  
- **Affiliations:**  
  - Komal Kumar, Tajamul Ashraf, Omkar Thawakar, Rao Muhammad Anwer, Hisham Cholakkal, Fahad Shahbaz Khan, and Salman Khan are with **Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi, UAE**.  
  - Mubarak Shah is with the **Center for Research in Computer Vision at the University of Central Florida, Orlando, FL, USA**.  
  - Ming-Hsuan Yang is with the **University of California at Merced, Merced, CA, USA**, and also with **Google DeepMind, Mountain View, CA, USA**.  
  - Philip H.S. Torr is with the **Department of Engineering Science, University of Oxford, Oxford, UK**.  

Feel free to ⭐ star and fork this repository to keep up with the latest advancements and contribute to the community.

<p align="center">
  <img src="./Images/teasor.jpg" width="45%" hieght="50%" />
<!--   <img src="./Images/methods.jpg" width="45%" height="50%" /> -->
</p>


---

## 📌 Contents  

| Section | Subsection |  
| ------- | ----------- |  
| [📖 Papers](#papers) | [Survey](#survey), [Theory](#theory), [Explainability](#explainability) |  
| [🤖 LLMs in RL](#llms-in-rl) | LLM-Augmented Reinforcement Learning |  
| [🏆 Reward Learning](#reward-learning) | [Human Feedback](#human-feedback), [Preference-Based RL](#preference-based-rl), [Intrinsic Motivation](#intrinsic-motivation) |  
| [🚀 Policy Optimization](#policy-optimization) | [Offline RL](#offline-rl), [Imitation Learning](#imitation-learning), [Hierarchical RL](#hierarchical-rl) |  
| [🧠 LLMs for Reasoning & Decision-Making](#llms-for-reasoning-and-decision-making) | [Causal Reasoning](#causal-reasoning), [Planning](#planning), [Commonsense RL](#commonsense-rl) |  
| [🌀 Exploration & Generalization](#exploration-and-generalization) | [Zero-Shot RL](#zero-shot-rl), [Generalization in RL](#generalization-in-rl), [Self-Supervised RL](#self-supervised-rl) |  
| [🤝 Multi-Agent RL (MARL)](#multi-agent-rl-marl) | [Emergent Communication](#emergent-communication), [Coordination](#coordination), [Social RL](#social-rl) |  
| [⚡ Applications & Benchmarks](#applications-and-benchmarks) | [Autonomous Agents](#autonomous-agents), [Simulations](#simulations), [LLM-RL Benchmarks](#llm-rl-benchmarks) |  
| [📚 Tutorials & Courses](#tutorials-and-courses) | [Lectures](#lectures), [Workshops](#workshops) |  
| [🛠️ Libraries & Implementations](#libraries-and-implementations) | Open-Source RL-LLM Frameworks |  
| [🔗 Other Resources](#other-resources) | Additional Research & Readings |  

---

# 📖 Papers  

## 🔍 Survey  

| Title | Publication Date | Link |
|---------------------------------|----------------|---------------------------------|
| From System 1 to System 2: A Survey of Reasoning Large Language Models | 25 Feb 2025 | [Arxiv](https://arxiv.org/abs/2502.17419) |
| Towards Large Reasoning Models: A Survey of Reinforced Reasoning with Large Language Models | 16 Jan 2025 | [Arxiv](https://arxiv.org/abs/2501.09686) |
| Reasoning with Large Language Models, a Survey | 16 July 2024 | [Arxiv](https://arxiv.org/abs/2407.11511) |
| Survey on Large Language Model-Enhanced Reinforcement Learning: Concept, Taxonomy, and Methods | 30 Mar 2024 | [Arxiv](https://arxiv.org/abs/2404.00282) |
| Reinforcement Learning Enhanced LLMs: A Survey | 5 Dec 2024 | [Arxiv](https://arxiv.org/abs/2412.10400) |
| Enhancing Code LLMs with Reinforcement Learning in Code Generation: A Survey | 29 Dec 2024 | [Arxiv](https://arxiv.org/abs/2412.20367) |
| Large Language Models: A Survey of Their Development, Capabilities, and Applications | 15 Jan 2025 | [Springer](https://link.springer.com/article/10.1007/s10115-024-02310-4) |
| A Survey on Multimodal Large Language Models | 10 Feb 2025 | [Oxford Academic](https://academic.oup.com/nsr/article/11/12/nwae403/7896414) |
| Large Language Models (LLMs): Survey, Technical Frameworks, and Future Directions | 20 Jul 2024 | [Springer](https://link.springer.com/article/10.1007/s10462-024-10888-y) |
| Using Large Language Models to Automate and Expedite Reinforcement Learning with Reward Machines | 11 Feb 2024 | [Arxiv](https://arxiv.org/abs/2402.07069) |
| ExploRLLM: Guiding Exploration in Reinforcement Learning with Large Language Models | 14 Mar 2024 | [Arxiv](https://arxiv.org/abs/2403.09583) |
| Reinforcement Learning Problem Solving with Large Language Models | 29 Apr 2024 | [Arxiv](https://arxiv.org/abs/2404.18638) |
| A Survey on Large Language Models for Reinforcement Learning | 10 Dec 2023 | [Arxiv](https://arxiv.org/abs/2312.04567) |
| Large Language Models as Decision-Makers: A Survey | 23 Aug 2023 | [Arxiv](https://arxiv.org/abs/2308.11749) |
| A Survey on Large Language Model Alignment Techniques | 6 May 2023 | [Arxiv](https://arxiv.org/abs/2305.00921) |
| Reinforcement Learning with Human Feedback: A Survey | 12 April 2023 | [Arxiv](https://arxiv.org/abs/2304.04989) |
| Reasoning with Large Language Models: A Survey | 14 Feb 2023 | [Arxiv](https://arxiv.org/abs/2302.06476) |
| A Survey on Foundation Models for Decision Making | 9 Jan 2023 | [Arxiv](https://arxiv.org/abs/2301.04150) |
| Large Language Models in Reinforcement Learning: Opportunities and Challenges | 5 Dec 2022 | [Arxiv](https://arxiv.org/abs/2212.09142) |


---

## 🤖 LLMs in RL  

- **"Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search"** | 08-02-2025 | [[Paper](https://arxiv.org/abs/2502.02508)]  
- **"DeepScaleR: Surpassing O1-Preview with a 1.5B Model by Scaling RL"** | 08-02-2025 | [[Paper](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2)]  
- **"QLASS: Boosting Language Agent Inference via Q-Guided Stepwise Search"** | 08-02-2025 | [[Paper](https://arxiv.org/abs/2502.02584)]  
- **"Process Reinforcement through Implicit Rewards"** | 04-02-2025 | [[Paper](https://arxiv.org/abs/2502.01456)]  
- **"Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling"** | 29-01-2025 | [[Paper](https://arxiv.org/abs/2501.11651)]  
- **"Challenges in Ensuring AI Safety in DeepSeek-R1 Models: The Shortcomings of Reinforcement Learning Strategies"** | 30-01-2025 [[Paper](https://arxiv.org/abs/2501.17030)]  
- **"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"** | 26-01-2025 | [[Paper](https://arxiv.org/abs/2501.12948)]  
- **"Kimi k1.5: Scaling Reinforcement Learning with LLMs"** | 25-01-2025 | [[Paper](https://arxiv.org/abs/2501.12599)]  
- **"Does RLHF Scale? Exploring the Impacts From Data, Model, and Method"** | 18-12-2024 | [[Paper](https://arxiv.org/abs/2412.06000)]  
- **"Offline Reinforcement Learning for LLM Multi-Step Reasoning"** | 29-12-2024 | [[Paper](https://arxiv.org/abs/2412.16145)]  
- **"ReFT: Representation Finetuning for Language Models"** | 10-07-2024 | [[Paper](https://aclanthology.org/2024.acl-long.410.pdf)]  
- **"Deepseekmath: Pushing the Limits of Mathematical Reasoning in Open Language Models"** | 02-02-2024 | [[Paper](https://arxiv.org/abs/2402.03300)]  
- **"Reasoning with Reinforced Functional Token Tuning"** | 15-02-2025 | [[Paper](https://arxiv.org/abs/2502.13389)]  
- **"Value-Based Deep RL Scales Predictably"** | 07-02-2025 | [[Paper](https://arxiv.org/abs/2502.04327)]  
- **"InfAlign: Inference-aware Language Model Alignment"** | 30-12-2024 | [[Paper](https://arxiv.org/abs/2412.19792)]  
- **"LIMR: Less is More for RL Scaling"** | 12-02-2025 | [[Paper](https://arxiv.org/abs/2502.11886)]  
- **"A Survey on Feedback-based Multi-step Reasoning for Large Language Models on Mathematics"** | 14-02-2025 | [[Paper](https://arxiv.org/abs/2502.143)]  
 

---

## 🏆 Reward Learning (Process Reward Models)

* PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. [[Paper]](https://arxiv.org/abs/2501.03124) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding [[Paper]](https://arxiv.org/abs/2501.07861) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* The Lessons of Developing Process Reward Models in Mathematical Reasoning. [[Paper]](https://arxiv.org/abs/2501.07301) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* ToolComp: A Multi-Tool Reasoning & Process Supervision Benchmark. [[Paper]](https://arxiv.org/abs/2501.01290) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* AutoPSV: Automated Process-Supervised Verifier [[Paper]](https://openreview.net/forum?id=eOAPWWOGs9) ![](https://img.shields.io/badge/NeurIPS-2024-blue)
* ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search [[Paper]](https://openreview.net/forum?id=8rcFOqEud5) ![](https://img.shields.io/badge/NeurIPS-2024-blue)
* Free Process Rewards without Process Labels. [[Paper]](https://arxiv.org/abs/2412.01981) ![](https://img.shields.io/badge/arXiv-2024.12-red)
* Outcome-Refining Process Supervision for Code Generation [[Paper]](https://arxiv.org/abs/2412.15118) ![](https://img.shields.io/badge/arXiv-2024.12-red)
* Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations [[Paper]](https://aclanthology.org/2024.acl-long.510/) ![](https://img.shields.io/badge/ACL-2024-blue)
* OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning [[Paper]](https://aclanthology.org/2024.findings-naacl.55/) ![](https://img.shields.io/badge/ACL_Findings-2024-blue)
* Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs [[Paper]](https://arxiv.org/abs/2406.18629) ![](https://img.shields.io/badge/arXiv-2024.06-red)
* Let's Verify Step by Step. [[Paper]](https://arxiv.org/abs/2305.20050) ![](https://img.shields.io/badge/arXiv-2024.05-red)
* Improve Mathematical Reasoning in Language Models by Automated Process Supervision [[Paper]](https://arxiv.org/abs/2306.05372) ![](https://img.shields.io/badge/arXiv-2023.06-red)
* Making Large Language Models Better Reasoners with Step-Aware Verifier [[Paper]](https://arxiv.org/abs/2206.02336) ![](https://img.shields.io/badge/arXiv-2023.06-red)
* Solving Math Word Problems with Process and Outcome-Based Feedback [[Paper]](https://arxiv.org/abs/2211.14275) ![](https://img.shields.io/badge/arXiv-2022.11-red)
* Uncertainty-Aware Step-wise Verification with Generative Reward Models [[Paper]](https://arxiv.org/abs/2502.11250) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence [[Paper]](https://www.arxiv.org/abs/2502.13943) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* Self-Consistency of the Internal Reward Models Improves Self-Rewarding Language Models [[Paper]](https://www.arxiv.org/abs/2502.08922) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling [[Paper]](https://arxiv.org/abs/2502.06703) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems [[Paper]](https://arxiv.org/abs/2502.19328) ![](https://img.shields.io/badge/arXiv-2025.02-red)

---

## 🚀 Policy Optimization  

- **"Decision Transformer: Reinforcement Learning via Sequence Modeling"** - Chen et al. (2021) [[Paper](https://arxiv.org/abs/2106.01345)]  
- **"Offline RL with LLMs as Generalist Memory"** - Tian et al. (2023) [[Paper](https://arxiv.org/abs/2302.02096)]  

---

## Part 8: Explainability
* Agents Thinking Fast and Slow: A Talker-Reasoner Architecture [[Paper]](https://openreview.net/forum?id=xPhcP6rbI4) ![](https://img.shields.io/badge/NeurIPS_WorkShop-2024-blue)
* What Happened in LLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective [[Paper]](https://arxiv.org/abs/2410.23743) ![](https://img.shields.io/badge/arXiv-2024.10-red)
* When a Language Model is Optimized for Reasoning, Does It Still Show Embers of Autoregression? An Analysis of OpenAI o1 [[Paper]](https://arxiv.org/abs/2410.01792) ![](https://img.shields.io/badge/arXiv-2024.10-red)
* The Impact of Reasoning Step Length on Large Language Models [[Paper]](https://arxiv.org/abs/2401.04925) ![](https://img.shields.io/badge/arXiv-2024.08-red)
* Distilling System 2 into System 1 [[Paper]](https://arxiv.org/abs/2407.06023) ![](https://img.shields.io/badge/arXiv-2024.07-red)
* System 2 Attention (is something you might need too) [[Paper]](https://arxiv.org/abs/2311.11829) ![](https://img.shields.io/badge/arXiv-2023.11-red)
* Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Thought [[Paper]](https://arxiv.org/abs/2501.04682) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* LlamaV-o1: Rethinking Step-by-step Visual Reasoning in LLMs [[Paper]](https://arxiv.org/abs/2501.06186) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* Two Heads Are Better Than One: Dual-Model Verbal Reflection at Inference-Time [[Paper]](https://arxiv.org/abs/2502.19230) ![](https://img.shields.io/badge/arXiv-2025.02-red)
## Part 9: Multimodal Agent related Slow-Fast System
* Diving into Self-Evolving Training for Multimodal Reasoning [[Paper]](https://arxiv.org/abs/2412.17451) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* Visual Agents as Fast and Slow Thinkers [[Paper]](https://openreview.net/forum?id=ncCuiD3KJQ) ![](https://img.shields.io/badge/ICLR-2025-blue)
* Virgo: A Preliminary Exploration on Reproducing o1-like MLLM [[Paper]](https://arxiv.org/abs/2501.01904) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* Scaling Inference-Time Search With Vision Value Model for Improved Visual Comprehension [[Paper]](https://arxiv.org/pdf/2412.03704) ![](https://img.shields.io/badge/arXiv-2024.12-red)
* Slow Perception: Let's Perceive Geometric Figures Step-by-Step [[Paper]](https://arxiv.org/abs/2412.20631) ![](https://img.shields.io/badge/arXiv-2024.12-red)
* AtomThink: A Slow Thinking Framework for Multimodal Mathematical Reasoning [[Paper]](https://arxiv.org/abs/2411.11930) ![](https://img.shields.io/badge/arXiv-2024.11-red)
* LLaVA-o1: Let Vision Language Models Reason Step-by-Step [[Paper]](https://arxiv.org/abs/2411.10440) ![](https://img.shields.io/badge/arXiv-2024.11-red)
* Vision-Language Models Can Self-Improve Reasoning via Reflection [[Paper]](https://arxiv.org/abs/2411.00855) ![](https://img.shields.io/badge/arXiv-2024.11-red)
* I Think, Therefore I Diffuse: Enabling Multimodal In-Context Reasoning in Diffusion Models [[Paper]](https://arxiv.org/abs/2502.10458) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* RAG-Gym: Optimizing Reasoning and Search Agents with Process Supervision [[Paper]](https://arxiv.org/abs/2502.13957) ![](https://img.shields.io/badge/arXiv-2025.02-red)
## Part 10: Benchmark and Datasets
* Big-Math: A Large-Scale, High-Quality Math Dataset for Reinforcement Learning in Language Models [[Paper]](https://arxiv.org/abs/2502.17387) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models [[Paper]](https://arxiv.org/abs/2501.03124) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs [[Paper]](https://openreview.net/forum?id=GN2qbxZlni) ![](https://img.shields.io/badge/NeurIPS-2024-blue)
* Do NOT Think That Much for 2+3=? On the Overthinking of o1-like LLMs [[Paper]](https://arxiv.org/abs/2412.21187) ![](https://img.shields.io/badge/arXiv-2024.12-red)
* A Preliminary Study of o1 in Medicine: Are We Closer to an AI Doctor? [[Paper]](https://arxiv.org/abs/2409.15277) ![](https://img.shields.io/badge/arXiv-2024.09-red)
* EquiBench: Benchmarking Code Reasoning Capabilities of Large Language Models via Equivalence Checking [[Paper]](https://arxiv.org/abs/2502.12466) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* SuperGPQA: Scaling LLM Evaluation across 285 Graduate Disciplines [[Paper]](https://arxiv.org/abs/2502.14739) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* Multimodal RewardBench: Holistic Evaluation of Reward Models for Vision Language Models [[Paper]](https://arxiv.org/abs/2502.14191) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI [[Paper]](https://arxiv.org/abs/2411.04872) ![](https://img.shields.io/badge/arXiv-2024.11-red)
* Evaluation of OpenAI o1: Opportunities and Challenges of AGI [[Paper]](https://arxiv.org/abs/2409.18486) ![](https://img.shields.io/badge/arXiv-2024.09-red)
* MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations [[Paper]](https://arxiv.org/abs/2502.06453) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* LongReason: A Synthetic Long-Context Reasoning Benchmark via Context Expansion [[Paper]](https://arxiv.org/abs/2501.15089) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* Humanity's Last Exam [[Paper]](https://arxiv.org/abs/2501.14249) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* LR<sup>2</sup>Bench: Evaluating Long-chain Reflective Reasoning Capabilities of Large Language Models via Constraint Satisfaction Problems [[Paper]](https://arxiv.org/abs/2502.17848) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* BIG-Bench Extra Hard [[Paper]](https://arxiv.org/abs/2502.19187) ![](https://img.shields.io/badge/arXiv-2025.02-red)

## Part 11: Reasoning and Safety
* OverThink: Slowdown Attacks on Reasoning LLMs [[Paper]](https://arxiv.org/abs/2502.02542) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* GuardReasoner: Towards Reasoning-based LLM Safeguards [[Paper]](https://arxiv.org/abs/2501.18492) ![](https://img.shields.io/badge/arXiv-2025.01-red)
* SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities [[Paper]](https://arxiv.org/abs/2502.12025) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* ThinkGuard: Deliberative Slow Thinking Leads to Cautious Guardrails [[Paper]](https://arxiv.org/abs/2502.13458) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities [[Paper]](https://arxiv.org/abs/2502.12025) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking [[Paper]](https://arxiv.org/abs/2502.12893) ![](https://img.shields.io/badge/arXiv-2025.02-red)
* BoT: Breaking Long Thought Processes of o1-like Large Language Models through Backdoor Attack [[Paper]](https://arxiv.org/abs/2502.12202) ![](https://img.shields.io/badge/arXiv-2025.02-red)


---
## 🚀 RL & LLM Fine-Tuning Repositories

| #  | Repository & Link                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [**RL4VLM**](https://github.com/RL4VLM/RL4VLM) <br><br> _Archived & Read-Only as of December 15, 2024_       | Offers code for fine-tuning large vision-language models as decision-making agents via RL. Includes implementations for training models with task-specific rewards and evaluating them in various environments.                                                                                                                                                                                                                                                                                                         |
| 2  | [**LlamaGym**](https://github.com/KhoomeiK/LlamaGym)                                                      | Simplifies fine-tuning large language model (LLM) agents with online RL. Provides an abstract `Agent` class to handle various aspects of RL training, allowing for quick iteration and experimentation across different environments.                                                                                                                                                                                                                                                                                      |
| 3  | [**RL-Based Fine-Tuning of Diffusion Models for Biological Sequences**](https://github.com/masa-ue/RLfinetuning_Diffusion_Bioseq) | Accompanies a tutorial and review paper on RL-based fine-tuning, focusing on the design of biological sequences (DNA/RNA). Provides comprehensive tutorials and code implementations for training and fine-tuning diffusion models using RL.                                                                                                                                                                                                                                     |
| 4  | [**LM-RL-Finetune**](https://github.com/zhixuan-lin/LM-RL-finetune)                                       | Aims to improve KL penalty optimization in RL fine-tuning of language models by computing the KL penalty term analytically. Includes configurations for training with Proximal Policy Optimization (PPO).                                                                                                                                                                                                                                                                                                                     |
| 5  | [**InstructLLaMA**](https://github.com/michaelnny/InstructLLaMA)                                           | Implements pre-training, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF) to train and fine-tune the LLaMA2 model to follow human instructions, similar to InstructGPT or ChatGPT.                                                                                                                                                                                                                                                                                                       |
| 6  | [**SEIKO**](https://github.com/zhaoyl18/SEIKO)                                                             | Introduces a novel RL method to efficiently fine-tune diffusion models in an online setting. Its techniques outperform baselines such as PPO, classifier-based guidance, and direct reward backpropagation for fine-tuning Stable Diffusion.                                                                                                                                                                                                                                                                              |
| 7  | [**TRL (Train Transformer Language Models with RL)**](https://github.com/huggingface/trl)                  | A state-of-the-art library for post-training foundation models using methods like Supervised Fine-Tuning (SFT), Proximal Policy Optimization (PPO), GRPO, and Direct Preference Optimization (DPO). Built on the 🤗 Transformers ecosystem, it supports multiple model architectures and scales efficiently across hardware setups.                                                                                                                                                                                     |
| 8  | [**Fine-Tuning Reinforcement Learning Models as Continual Learning**](https://github.com/BartekCupial/finetuning-RL-as-CL) | Explores fine-tuning RL models as a forgetting mitigation problem (continual learning). Provides insights and code implementations to address forgetting in RL models.                                                                                                                                                                                                                                                                                                                                                        |
| 9  | [**RL4LMs**](https://github.com/allenai/RL4LMs)                                                            | A modular RL library to fine-tune language models to human preferences. Rigorously evaluated through 2000+ experiments using the GRUE benchmark, ensuring robustness across various NLP tasks.                                                                                                                                                                                                                                                                                                                             |
| 10 | [**Lamorel**](https://github.com/flowersteam/lamorel)                                                      | A high-throughput, distributed architecture for seamless LLM integration in interactive environments. While not specialized in RL or RLHF by default, it supports custom implementations and is ideal for users needing maximum flexibility.                                                                                                                     |
| 11 | [**LLM-Reverse-Curriculum-RL**](https://github.com/WooooDyy/LLM-Reverse-Curriculum-RL)                     | Implements the ICML 2024 paper *"Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning"*. Focuses on enhancing LLM reasoning capabilities using a reverse curriculum RL approach.                                                                                                                                                                                                                                                  |
| 12 | [**veRL**](https://github.com/volcengine/verl)                                                             | A flexible, efficient, and production-ready RL training library for large language models (LLMs). Serves as the open-source implementation of the HybridFlow framework and supports various RL algorithms (PPO, GRPO), advanced resource utilization, and scalability up to 70B models on hundreds of GPUs. Integrates with Hugging Face models, supervised fine-tuning, and RLHF with multiple reward types.                                                  |
| 13 | [**trlX**](https://github.com/CarperAI/trlx)                                                               | A distributed training framework for fine-tuning large language models (LLMs) with reinforcement learning. Supports both Accelerate and NVIDIA NeMo backends, allowing training of models up to 20B+ parameters. Implements PPO and ILQL, and integrates with CHEESE for human-in-the-loop data collection.                                                                                                                                                                                              |
| 14 | [**Okapi**](https://github.com/nlp-uoregon/Okapi)                                                          | A framework for instruction tuning in LLMs with RLHF, supporting 26 languages. Provides multilingual resources such as ChatGPT prompts, instruction datasets, and response ranking data, along with both BLOOM-based and LLaMa-based models and evaluation benchmarks.                                                                                                                                                                                                                                                 |
| 15 | [**LLaMA-Factory**](https://github.com/hiyouga/LLaMA-Factory)                                              | *Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)*. Supports a wide array of models (e.g., LLaMA, LLaVA, Qwen, Mistral) with methods including pre-training, multimodal fine-tuning, reward modeling, PPO, DPO, and ORPO. Offers scalable tuning (16-bit, LoRA, QLoRA) with advanced optimizations and logging integrations, and provides fast inference via API, Gradio UI, and CLI with vLLM workers.                                                 |

---
## ⚡ Applications & Benchmarks  

- **"AutoGPT: LLMs for Autonomous RL Agents"** - OpenAI (2023) [[Paper](https://arxiv.org/abs/2304.03442)]  
- **"Barkour: Benchmarking LLM-Augmented RL"** - Wu et al. (2023) [[Paper](https://arxiv.org/abs/2305.12377)]  

---

## 📚 Tutorials & Courses  

- 🎥 **Deep RL Bootcamp (Berkeley)** [[Website](https://sites.google.com/view/deep-rl-bootcamp/)]  
- 🎥 **DeepMind RL Series** [[Website](https://deepmind.com/learning-resources)]  

---

## 🛠️ Libraries & Implementations  

- 🔹 [Decision Transformer (GitHub)](https://github.com/kzl/decision-transformer)  
- 🔹 [ReAct (GitHub)](https://github.com/ysymyth/ReAct)  
- 🔹 [RLHF (GitHub)](https://github.com/openai/lm-human-preferences)  

---

## 🔗 Other Resources  

- [LLM for RL Workshop at NeurIPS 2023](https://neurips.cc)  
- [OpenAI Research Blog on RLHF](https://openai.com/research)  

---

## 📌 Contributing  

Contributions are welcome! If you have relevant papers, code, or insights, feel free to submit a pull request.  




## Citation

If you find our work useful or use it in your research, please consider citing:

```bibtex
@misc{kumar2025llmposttrainingdeepdive,
      title={LLM Post-Training: A Deep Dive into Reasoning Large Language Models}, 
      author={Komal Kumar and Tajamul Ashraf and Omkar Thawakar and Rao Muhammad Anwer and Hisham Cholakkal and Mubarak Shah and Ming-Hsuan Yang and Phillip H. S. Torr and Salman Khan and Fahad Shahbaz Khan},
      year={2025},
      eprint={2502.21321},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.21321}, 
}
```
