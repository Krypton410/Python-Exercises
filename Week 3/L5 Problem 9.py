def semordnilapWrapper(str1, str2):

    def semordnilap(str1, str2):

        if (len(str1) != len(str2)):
            return False
        elif (len(str1) == 1):
            return str1 == str2
        else:
            return ((str1[-1] == str2[0]) and (semordnilap(str1[:-1],str2[1:])))
 

        if len(str1) == 1 or len(str2) == 1:
            return False

        return False
 
    return semordnilap(str1, str2)
 
print semordnilapWrapper('nametag', 'gateman')
print semordnilapWrapper('dog', 'god')
print semordnilapWrapper('live', 'evil')
print semordnilapWrapper('desserts', 'stressed')
print semordnilapWrapper('220', '022')

