import sys

def preprocessing_xml_with_chunk_tag(inputfile):

	inputfile_handler = open(inputfile)
	
	sentence_tags_tuples_list = []
	words_list = []
	tags_list = []

	for line in inputfile_handler.readlines():
		splitted_sentence = line.split()
		
		if line.strip() == "</Sentence>":
			sentence_tuple = (words_list, tags_list)
			sentence_tags_tuples_list.append(sentence_tuple)
			words_list = []
			tags_list = []

		if len(splitted_sentence) < 4:
		 	continue

		pos_tag = str(splitted_sentence[2])
		last_element = splitted_sentence[-1]
		word =  last_element[6:-2]

		if len(word) > 1 and word[-1].isdigit():
			word = word[:-1]

		words_list.append(word)
		tags_list.append(pos_tag)

	return sentence_tags_tuples_list



def preprocessing_xml_word_pos_tag(inputfile):

	inputfile_handler = open(inputfile)
	
	sentence_tags_tuples_list = []
	words_list = []
	tags_list = []

	for line in inputfile_handler.readlines():
		splitted_sentence = line.split()
		
		if line.strip() == "</Sentence>":
			sentence_tuple = (words_list, tags_list)
			sentence_tags_tuples_list.append(sentence_tuple)
			words_list = []
			tags_list = []

		if len(splitted_sentence) != 3 or splitted_sentence[0][:8] == "<Corpora":
		 	continue

		pos_tag = str(splitted_sentence[-1])
		word =  str(splitted_sentence[1])

		words_list.append(word)
		tags_list.append(pos_tag)

	return sentence_tags_tuples_list


def preprocessing_xml_word_underscore_tag(inputfile):

	inputfile_handler = open(inputfile)
	
	sentence_tags_tuples_list = []
	words_list = []
	tags_list = []

	for line in inputfile_handler.readlines():
		
		if line.strip() == "</Sentence>":
			sentence_tuple = (words_list, tags_list)
			sentence_tags_tuples_list.append(sentence_tuple)
			words_list = []
			tags_list = []

		if line.strip()[0] == '<':
		 	continue


		splitted_sentence = line.split()

		for pair in splitted_sentence:
			word, pos_tag = pair.split('_')
			words_list.append(word)
			tags_list.append(pos_tag)

	return sentence_tags_tuples_list

if __name__ == "__main__":


	processed_sentences_list = []
	partial_list = preprocessing_xml_with_chunk_tag(sys.argv[1])
	processed_sentences_list.extend(partial_list)
	partial_list = preprocessing_xml_with_chunk_tag(sys.argv[2])
	processed_sentences_list.extend(partial_list)
	partial_list = preprocessing_xml_word_pos_tag(sys.argv[3])
	processed_sentences_list.extend(partial_list)
	partial_list = preprocessing_xml_word_underscore_tag(sys.argv[4])
	processed_sentences_list.extend(partial_list)

	outputfile_handler = open(sys.argv[5], mode='w')
	print(len(processed_sentences_list))
	for _tuple in processed_sentences_list:
		outputfile_handler.write(str(_tuple[0])+"\n"+str(_tuple[1])+"\n\n")
