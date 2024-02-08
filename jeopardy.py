import pandas as pd
pd.set_option('display.max_colwidth', None)

# 1
data = pd.read_csv('jeopardy.csv')
# 2
data.columns= data.columns.str.lower()
data.columns= data.columns.str.strip()
data.rename(columns={'show number':'show_number','air date':'air_date'},inplace=True)
# print(data)

# 3
#Sample solution
def filter_data(data, words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return data.loc[data["question"].apply(filter)]

answer = filter_data(data, ['England', 'King'])

def my_filter(data, listofwords):
    result = data
    for word in listofwords:
        result = result[result.question.str.contains(word, case= False)]


    return result.reset_index()

#Check for differences between filter_data and my_filter
differece = pd.concat([answer, my_filter(data, ['England', 'King'])]).drop_duplicates(keep= False)

#mean calculation function
def mean_cal(df):
    result = df.value.str.strip('$').str.replace(',','').apply(lambda x: float(x) if x != "None" else 0)

    return result.mean()

#find the count of unique answer
def unique_count(df_column):
    return df_column.nunique()

#How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
df_computer = my_filter(data, ['computer'])
df_computer_90s = df_computer[df_computer.air_date.apply(lambda x: x[0:3] == '199')]
df_computer_20s = df_computer[df_computer.air_date.apply(lambda x: x[0:2] == '20')]
num_of_computer_use = abs(len(df_computer_90s) - len(df_computer_20s))

#"Literature" in Single Jeopardy or Double Jeopardy? Ans: Double Jeopardy
literature = data[data.category.apply(lambda x: 'literature' in x.lower())].reset_index()
literature_pivot = literature.pivot(index= 'index', columns= 'round')['air_date']
print(data.head())