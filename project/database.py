import csv


class Database:

    def __init__(self):
        """ Initialize """
        self.data = self.read_file()

    def read_file(self):
        """ read file from data.csv then get data to a list  """

        read_data = []
        with open('data.csv', 'r') as f:
            rows = csv.DictReader(f)
            for r in rows:
                read_data.append(r)
        return read_data

    def get_score(self, name: str):
        """
        get score all round from players
        :param name
        :type name:str

        """
        for row in self.data:
            if row['name'] == name:
                return int(row['score'])
        return None

    def update_best_score(self, name, score):
        """ update lasted score or highest score of players to best score
         and get new data to CSV file """

        new_data = {'name': name, 'score': score}
        for i in self.data:
            if i['name'] == new_data['name']:
                # replace best_score
                if int(i['score']) < score:
                    i['score'] = score
                    break
        else:
            self.data.append(new_data)

        self.write_data()

    def write_data(self):
        """ write new data in CSV file  """

        header = ['name', 'score']
        with open('data.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for r in self.data:
                writer.writerow(r)


if __name__ == '__main__':
    data = Database()
    data.write_data()

