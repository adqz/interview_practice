import pandas as pd

def convert_txt_to_csv(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  
  df = pd.DataFrame(columns = ['number', 'name', 'level'])
  for i, line in enumerate(lines):
    words = line.split()
    number, name, level = words[0], ' '.join(words[1:-2]), words[-1]
    # print(number, '\t', name,'\t', level)
    df.loc[i,:] = number, name, level
  # print(df)
  df.to_csv(filename[0:-3]+'.csv', index=False)

if __name__ == '__main__':
  convert_txt_to_csv('google_questions.txt')