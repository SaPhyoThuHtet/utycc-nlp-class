# Myanmar POS Tagging Based on Machine Translation

### Abstract
• This project compares the performances achieved by Phrase-Based Statistical 
Machine Translation system(PBSMT), Neural Machine Translation based on 
sequence model of LSTM (Long Short Term Memory), and Attention-Based Neural 
Machine Translation systems (NMT) when translating Part-Of-Speech tagging (POS 
tagging) in Myanmar Language. <br>
• Part of speeches are very fundamental in a language and various languages had 
done in tagging part-of-speech and the use of tag sets vary upon each own 
language. <br>
• Important in Linguistics and part of speech tags can be used in building of 
Parse-tree(used in NERs) and for lemmatizers and many other NLP tasks. 
• The systems are built on a parallel Myanmar-POS tagging corpus with word 
segmented 10k text. <br>
• Through the research, PBSMT outperforms NMT. PBSMT also has a much higher 
evaluation score in  comparison. <br>
• Experiment's performances are evaluated with RIBES score, BLEU score, and 
ChrF++.<br>


### Introduction

Part of speech is a category to which a word is assigned by its syntactic functions and so the POS tagging is the activity of marking up a word in a text (corpus) as corresponding to a particular part of speech. Part of Speech tagging (also known as Grammatical tagging) is one of the most important NLP research processes. POS also is an important port in Linguistics. As it has a relationship with adjacent and related words in a phrase, sentence, or paragraph, Part-Of-Speech Tagging stands as a fundamental role in NLP research processes. Myanmar is one of the most spoken languages in Myanmar by the people in plain and also a sub-language for most people of the hills and belongs to the subfamily of Sino-Tibetan languages.

Myanmar is one of the under-resourced languages and there is no exact rule for word boundaries. Myanmar Language also needs to be POS tagged(Grammatical tagging). Like other translations (E.g. English to Spanish), Myanmar and POS tags can use the machine translation approach. Myanmar sentence is input as source language and POS would be the target language. For example,
 
ဦးသန့် အား ၎င်း မွေးဖွား ရာ ပန်းတနော် မြို့ ကို ရည်စူး ၍ ပန်းတနော် ဦးသန့် ဟု အမည်တွင် ခဲ့ သည် ။
n ppm pron v part n n ppm v conj n n part v part ppm punc
