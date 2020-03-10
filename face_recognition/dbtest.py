from database import Database

if __name__=="__main__":
    db=Database()

    #db.addPerson('person2','{name: "abcd"}')

    persons=db.getPerson(2)

    # print(persons)
    # print(type(persons))

    for p in persons:
        print(p[0],p[1],p[2],p[3])

    db.close()
