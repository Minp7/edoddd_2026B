''' 
NOTAS: 
1.Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero 
de estudiante 
2.Es ver cuanto crece el numero de 
operaciones en el algoritmo conforme 
creece el tamaño de la entrada 
agrego las bigO identificadas 
teniendo en cuenta la Cota superior asintotica 
O(n) + O(4) = O(n+4) = O(n)
'''
student_list_01 = ['Fer mi amor bot','pau','alex','poncho']
student_list_02 = ['toby','tache','zuzu greñuda','Shadow']

#verificando presencia de estudiante 
def check_student(input_student, student_list):
    for student in student_list: 
        if input_student == student:
            print("✔ Estudiante encontrado")
            return student
        #si no encuentro al estudiante
    print("🤣 Estudiante no encontrado")
    return None 

#Probando algoritmo 
check_student('pau', student_list_02) 