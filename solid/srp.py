# SRP - Single Responsible Principle

class Journal:
    def __init__(self):
        self.__entries = []

    def add_entry(self, text):
        self.__entries.append(text)

    def remove_entry(self, pos):
        del self.__entries[pos]

    def __str__(self):
        return '\n'.join(self.__entries)


# PersistnceManaeger USE-A journal
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Usmiechnalem sie dzisaj")
j.add_entry("Nie usmiechnalem sie dzisiaj")
PersistenceManager().save_to_file(j, 'journal.txt')
print(j)

