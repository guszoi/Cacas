import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    student_data_e: list[int] = []
    student_data_o: list[int] = []
    for sublist in student_data:
        student_data_e.append(sublist[0])
        student_data_o.append(sublist[1])

    d = {'student_id': student_data_e, 'age': student_data_o}
    df = pd.DataFrame(data=d)
    return df

student_data: list[list[int]] =  [[1, 15], [2, 11], [3, 11], [4, 20] ]
print(student_data)
dfStudentData = createDataframe(student_data)
print(dfStudentData)

""" 
otra solucion
"""
# import pandas as pd
# import numpy as np
#
# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     return pd.DataFrame(data=np.array(student_data), columns=['student_id','age'])