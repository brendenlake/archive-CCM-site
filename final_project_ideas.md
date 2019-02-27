# Final Project Ideas

Here is a list of final project ideas organized by topic. For many of these ideas, a first-rate project would be a novel contribution to research in computational cognitive modeling. In the list below, each bullet point is a separate project idea.

## Neural networks - Memory

- **Extending the Interactive activation model to a new domain**. Implement the Interactive Activation (IAC) Model (McClelland, 1981) from scratch and study a domain of your choice, replacing the characters from the West Side Story with different items. That is, rather than using a network to encode the people and properties from the “Jets and Sharks” example (as in Homework 1 - Part A), create a network that encodes information about a different domain of your choice (items and properties). Study the phenomena covered in class, such as content addressability, graceful degradation, spontaneous generalization, and other properties etc. in your new domain. Study how the parameters of the IAC model affect the results.

**References**:  
McClelland, J. L. (1981). Retrieving general and specific information from stored knowledge of specifics. In Proceedings of the third annual meeting of the cognitive science society.

## Probabilistic graphical models - Memory

- **Interactive activation model as Bayesian inference**. Study the interactive activation model reimagined as a Bayesian network rather than a neural network (a directed graphical model). In particular, use a “naive Bayesian classifier,” using the hidden/instance value as the latent “class” and the properties such as name, age, occupation, etc. as a vector of “observations.” Encode the Jets and Sharks example from Homework 1 (Part A) inside the Bayesian network, add noise to the conditional distributions, and then study phenomena discussed in class such as content addressability, graceful degradation, spontaneous generalization, etc. in this probabilistic model. Discuss the relationship between the interactive activation model and probabilistic modeling, as outlined in McClelland (2013).

**References**:  
McClelland, J. L. (1981). Retrieving general and specific information from stored knowledge of specifics. In Proceedings of the third annual meeting of the cognitive science society.
McClelland, J. L. (2013). Integrating probabilistic models of perception and interactive neural networks: a historical and tutorial review. Frontiers in psychology, 4, 503.

# Neural networks - Semantic Cognition

- **Extending the semantic cognition model to a new domain**. Extend the Rogers and McClelland (2003) model of semantic cognition (Homework 1 - Part C) to a much larger dataset of semantic knowledge about objects and their properties, or to a new domain all together. For instance, you could train the network on hundreds of objects and their properties). Study the dynamics of differentiation in development (Lecture 2 Slides 67-68) or degradation when noise is added (Lecture 2 Slide 69).
- **Object recognition and development**. Train a convolutional neural network for object recognition on a standard dataset, such as ImageNet, MiniImageNet, CIFAR-100, etc. As in the Rogers and McClelland (Homework 1 - Part C) model, study the dynamics of differentiation in development (Lecture 2 Slides 67-68) or degradation when noise is added (Lecture 2 Slide 69). Do you get the same coarse-to-fine pattern of development in an object recognition system trained for image classification?
- **Question answering for semantic cognition**. Reimagine the Rogers and McClelland network for semantic cognition (Homework 1 - Part C) using a more contemporary neural network architecture for Question Answering. Rather than taking an “Item” layer and “Relation” layer as separate inputs and producing all of the appropriate properties on the “Attributes” layer, you would use a recurrent neural network (RNN) for question answering. This alternative architecture could simply take a yes/no question in natural language as an input, such as “Can a canary sing?”, encode the question as a vector with a RNN, and produce an answer using a single binary output unit (simply “Yes” vs. “No”). You could train this model to learn all of the same facts as the Rogers and McClelland model, or on a different set of facts. Study the dynamics of differentiation in development (Lecture 2 Slides 67-68) or degradation when noise is added (Lecture 2 Slide 69).
- **Semantic cognition model from images (optionally, with question answering)**. Add a visual “frontend” to the Rogers and McClelland model (R&M model; Homework 1 - Part C). The R&M model assumes very high-level knowledge and categorical processing of the input data (Input is “Canary”). Is this a reasonable assumption? Rather than assuming clean input through the “Item” input layer, train the R&M architecture with a convolutional neural network frontend to take an image as input (replacing the “Item” layer), a “Relation” just as before on the Relation LAyer, in order to produce “Attributes.” For a truly extraordinary project, combine the visual frontend with the Question-Answering idea from the bullet above, training a neural network for question answering from images. Study the dynamics of differentiation in development (Lecture 2 Slides 67-68) or degradation when noise is added (Lecture 2 Slide 69).

**References**  
McClelland, J. L., & Rogers, T. T. (2003). The parallel distributed processing approach to semantic cognition. Nature Reviews Neuroscience, 4(4), 310. 

# Neural networks - Language 

- **Large-scale learning of lexical classes**. Can you discover lexical classes with a large-scale recurrent neural network (RNN)? Train a more contemporary recurrent neural network architecture (such as a LSTM) on a next word prediction task given a sizeable corpus of text, including thousands of sentences. Can you replicate some of the results from Elman (1990), especially the hierarchical clustering results for discovering lexical categories (Lecture 3 Slide 21)?

- **Exploring lexical and grammatical structure in BERT or GPT2**. What do powerful pre-trained models learn about lexical and grammatical structure? Explore the learned representations of a state-of-the-art language model  (BERT, GPT2, etc.) in systematic ways, and discuss the learned representation in relation to how children may acquire this structure through learning.

**References**  
Elman, J. L. (1990). Finding structure in time. Cognitive science, 14(2), 179-211.
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.
Radford et al., (2019). Language Models are Unsupervised Multitask Learners. arXiv preprint.

## Neural networks - visual representations

- **Comparing human and convolutional network representations for images**. With a visual domain of your choice (objects, animals, cars, etc.), use the Peterson et al. (2016) study design to compare the image similarity ratings between people and a pre-trained deep convolutional neural network trained on image recognition (as you did in Homework 1 Part D). Or, using a visual domain of your choice, use the Lake et al. (2015) study design compare typicality ratings between people and a pre-trained deep convolutional neural network trained on image recognition.

**References**  
Lake, B. M., Zaremba, W., Fergus, R. and Gureckis, T. M. (2015). Deep Neural Networks Predict Category Typicality Ratings for Images. In Proceedings of the 37th Annual Conference of the Cognitive Science Society.
Peterson, J., Abbott, J., & Griffiths, T. (2016). Adapting Deep Network Features to Capture Psychological Representations. Presented at the 38th Annual Conference of the Cognitive Science Society.

## Bayesian modeling / Probabilistic programming - Number game

- **Probabilistic programming and the number game**. In your Homework 3 (Part A), you explored a Bayesian model of concept learning with the number game. A potential weakness of this model is that the hypotheses need to be explicitly defined and enumerated as a list. Can you devise a more compact language or grammar for defining the space of possible number concepts? It may be convenient to define the prior distribution as a probabilistic program. Feel free to change the hypothesis space -- in that the prior defined by the probabilistic program may include some or most of the current hypotheses, but also others. How does the model performance change as you change the hypothesis space? Does this new prior help us better understand where people’s prior may come from?

**References**  
Gerstenberg, T., & Goodman, N. (2012). Ping Pong in Church: Productive use of concepts in human probabilistic inference. In Proceedings of the Annual Meeting of the Cognitive Science Society.

## Bayesian modeling  -- Categorical perception
- **Applying the perceptual magnet model to a new domain.** Pick a new domain to apply the Bayesian account of the perceptual magnet effect to, such as objects, image data, or audio data. Collect behavioral judgments about the discrimination between pairs of stimuli, or through similarity ratings between pairs of stimuli. Can you fit the Bayesian model to explain the behavioral data?

**References**  
Feldman, N. H., & Griffiths, T. L. (2007). A rational account of the perceptual magnet effect. In Proceedings of the Annual Meeting of the Cognitive Science Society. (http://ling.umd.edu/~nhf/papers/PerceptualMagnet.pdf)

## Reinforcement learning and Deep Q-Learning
- **Extend the homework to combine RL with convolutional nets.**  In the RL homework you will use the Open AI gym to solve some dynamic control problems from simplified featural representations of the current world state.  However, recent advances in Deep RL allow you use to use raw pixel inputs as features.  One project idea would be to extend the approach in the homework to model learning from the raw pixels of the images.  If you approach that, it is important to maintain a human comparison or element to your project.  For instance, one interesting psychological aspect is to consider how if you alter or obscure parts of the game, it makes it easier or harder for people (while not changing the difficulty for your RL agent) as in the Dubey et al. (preprint) below.  To do this might require a little bit of hacking of the OpenAI environment and also asking your friends to play a few weird video games to measure their performance.

**References**  

The OpenAI Gym: https://gym.openai.com/envs/#atari

Dubey, R., Agrawal, P., Pathak, D., Griffiths, T. L., & Efros, A. A. (preprint). Investigating human priors for playing video games. In Proceedings of the 35th International Conference on Machine Learning (ICML 2018). https://rach0012.github.io/humanRL_website/ (paper and project website)

## Decision Making 

- **Modeling human decision making** - The choice prediction task is a Kaggle-style challenge problem where in human participants were given a huge number of choices between gambles. The space of the gambles aims to expose many of the features of human decision making irrationalities.  Each year there is a competition built around these problems along with a number of models which have been determined to be the “winner.”  You can attempt to your use data science and cognitive modeling skills to enter a new model into this competition (or replicating and existing one), evaluating its performance according to the same measures used in the original choice prediction challenge.

**References**  
The Choice Prediction Challenge website: https://cpc-18.com

Plonsky, Ori and Erev, Ido and Hazan, Tamir and Tennenholtz, Moshe, Psychological Forest: Predicting Human Behavior (May 19, 2016). Available at SSRN: https://ssrn.com/abstract=2816450 or http://dx.doi.org/10.2139/ssrn.2816450

## Categorization and Category Learning

**Contribute to open science!** As mentioned in the lecture on categorization there are a variety of different theories of how people learn categories and concepts from examples, and many of these models draw from similar approaches to machine classification.  Currently there is a community-led effort to implement all existing category learning models in R so they can be simultaneously compared to the same sets of human data patterns. While the project is well developed and documented there are many example models which have not yet been implement (some of which are actually somewhat easy).  One nice final project would be to read one of the papers listed below which describe a famous formal model of human categorization and implement it for submission to the catlearn R package.  This is best for a group with some expertise in R (as opposed to python).  If your group makes a report showing how this model does on the existing data set in catlearn it would make a nice final paper and by making a pull request against the catlearn package your work for class might live forever to help advance science!  You could also choose to implement these models in python in which case you could still make an impact by helping to verify the previous results (see below).

**References**:

Catlearn R pacakage: https://ajwills72.github.io/catlearn/

**Examples**:
- RULEX is a simple type of decision tree algorithm - Nosofsky, R. M., Palmeri, T. J., & McKinley, S. C. (1994). Rule-plus-exception model of classification learning. Psychological Review, 101(1), 53-79.[here](http://www.cogs.indiana.edu/nosofsky/pubs/1994_rmn-tjp-scm_pr_rule.pdf)

- ATRIUM is a hybrid rule and nearest neighbor/exemplar algorithm that is trained used backpropogation and gradient descent - Erickson, M. A., & Kruschke, J. K. (1998). Rules and exemplars in category learning. Journal of Experimental Psychology: General, 127(2), 107-140. [here](https://psycnet.apa.org/fulltext/1998-02301-001.html)

## Replicate and verify!

Psychology is largely an empirical science and thus findings need to be independently replicated before they should be widely accepted.  This is true for computational cognitive modeling as well.  A line of interesting final projects would be to pick a recent computational modeling paper and to re-implement and verify the results reported by the authors.  In doing this exercise you might come up with your own ideas about a feature to alter or change in their simulations that might be interesting.  A couple good sources for papers would be to look at the titles from the most recent Proceedings of the Cognitive Science society or a new journal called Computational Brain and Behavior.

**References**
- [Computational Brain and Behavior](https://www.springer.com/psychology/cognitive+psychology/journal/42113)
- [2018 Cognitive Science Society Proceedings](https://cognitivesciencesociety.org/wp-content/uploads/2019/01/cogsci18_proceedings.pdf)
- [10 classic papers in cognitive science](http://www.indiana.edu/~pcl/rgoldsto/cogsci/classics.html)
