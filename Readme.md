# Unsupervised-chunking-in-Indian-languages

## Introduction

•Chunking is a process of extracting phrases from unstructured text. Instead of just simple tokens which may not represent the actual meaning of the text, its advisable to use phrases such as “South Africa” as a single word instead of ‘South’ and ‘Africa’ separate words.

•Chunking works on top of POS tagging, it uses pos-tags as input and provides chunks as output.

## Problem statement

•We are provided with dataset of Hindi sentences with PoS (Part of speech) tagging.
•Chunking, or shallow-parsing, is a task that requires the identification of syntactic units which belong together, for example verbs and verbal auxiliaries are one chunk
•The aim of this project is to create a phrase based chunking algorithm for Indian Languages Chunking works on top of POS tagging, it uses pos-tags as input and provides chunks as output.

## Baselines

•For baseline we will be using nltk package which has the following functions/packages:

•ChunkedCorpusReader
•tag_pattern2re_pattern
•RegexpParser

•These also take as argument the chunk tag pattern in the form of regular expression.•Neural network models will also be used for baseline.  (CNN, RNN, Bi-LSTM)

## Unsupervised models

•We’ll be experimenting with unsupervised dependency parsing as most recent work (and progress) in unsupervised parsing has come from tree or phrase structure basedmodels, but there are compelling reasons to reconsider unsupervised dependency parsing as well.
•We’ll also be exploring autoencoders to be able to encode sentence into meaningful chunks.
•Lastly, K-means clustering to group related words into chunks will be experimented with.
