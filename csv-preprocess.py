import csv 

DATA_PATH = './data/dataset_new.csv'

def get_unique_genres() -> list[str]:
    results = set([])
    
    with open(DATA_PATH, encoding="utf8") as file_obj: 
        reader_obj = csv.DictReader(file_obj) 
        for row in reader_obj:
            try:
                results.add(row["track_genre"])
            except:
                print("problem with row:", row)
                
    return results


if __name__ == "__main__":
    print(get_unique_genres())