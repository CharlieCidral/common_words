import chardet
import collections

def most_common_words(file_name, words_to_exclude=[]):
    """
    Encontra as 20 palavras mais repetidas em um arquivo de texto.

    Args:
      file_name: O nome do arquivo de texto.
      words_to_exclude: Uma lista de palavras a serem desconsideradas.

    Returns:
      Uma lista das 20 palavras mais repetidas, exceto as palavras na lista 'words_to_exclude'.
    """

    with open(file_name, 'rb') as f:
        encoding = chardet.detect(f.read())['encoding']

    with open(file_name, 'r', encoding=encoding) as f:
        words = f.read().split()

    # Filtra as palavras que devem ser desconsideradas.
    words = [word for word in words if word.lower() not in map(str.lower, words_to_exclude)]

    # Conta o número de vezes que cada palavra ocorre.
    counts = collections.Counter(words)

    # Ordena as palavras pela contagem decrescente.
    most_common_words = counts.most_common(20)

    return most_common_words

if __name__ == '__main__':
    # List of words to be excluded
    words_to_exclude = ['de','a','que','o','em','é','um','para','e','uma','do','você','por','os','mais','com','$','-','da','no','se','não','as','eu','ou','dos','na','como','são','está','muito','mas','isso','ao','Agora,','nos','das','apenas','cada','Então,','sobre','sua','anos','seu','foi','vamos','ser','Bem,','até','cerca','pode','há','tem','seus','100','quando','dois','três','menos','esse','ano']  
    most_common_words = most_common_words('Business.txt', words_to_exclude)

    # Imprime as 20 palavras mais repetidas.
    for word, count in most_common_words:
        print(word, count)
