https://leetcode.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result_list = []
        cur_line_words = []
        cur_line_len = 0
        for word in words:
            #print(word)
            if cur_line_len + len(word) <= maxWidth:
                cur_line_words.append(word)
                cur_line_len +=1 + len(word)
                continue
            else:
                #print(cur_line_words)
                new_line = ""
                nr_words = len(cur_line_words)
                nr_spaces = maxWidth - sum([len(word) for word in cur_line_words])
                if nr_words == 1:
                    new_line = cur_line_words[0] + " " * nr_spaces
                else:
                    nr_slots = nr_words -1
                    print(cur_line_words, nr_spaces, nr_slots)
                    if nr_spaces % nr_slots == 0:
                        spaces = [" " * (nr_spaces // nr_slots)] * nr_slots
                    else:
                        q = nr_spaces // nr_slots
                        r = nr_spaces % nr_slots
                        spaces = [" " * (nr_spaces // nr_slots +1)] * r + \
                        [" "* (nr_spaces // nr_slots)] * (nr_slots -r)
                    new_line = cur_line_words.pop(0)
                    for space, new_word in zip(spaces, cur_line_words):
                        new_line += space
                        new_line += new_word
                result_list += [new_line]
                cur_line_words = [word]
                cur_line_len = len(word) + 1
        new_line = ""
        nr_words = len(cur_line_words)
        nr_spaces = maxWidth - sum(len(word) for word in cur_line_words)
        spaces = [" "] * (nr_words -1) + [" " * (nr_spaces - nr_words +1)]
        for word, space in zip(cur_line_words, spaces):
            new_line += word
            new_line += space
        result_list += [new_line]
        return result_list
