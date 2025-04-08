class Patient{
    constructor(name,age){
        this.name = name
        this.age = age
    }
}

class MEEEDICCC{
    constructor(name,age,profession,receptionTime){
        this.name = name
        this.age = age
        this.profession = profession
        this.receptionTime = receptionTime
    }
}

class Ospitel{
    constructor(){
        this.pateientLitht = []
        this.dfodctorLitht = []
    }
    
    bwelarghALLPatients(){
        for(let i = 0; i < this.pateientLitht.length; i++){
            console.log(this.pateientLitht[i])
        }
    }
    bwelarghALLMuhdicss(){
        for(let i = 0; i < this.dfodctorLitht.length; i++){
            console.log(this.dfodctorLitht[i])
        }
    }
    bwelarghSurchMuhdicss(){
        let adshf = prompt("BWELLRAAAGHG!!! ")
        console.log(this.dfodctorLitht.find(({ name }) => name === adshf).receptionTime)
    }
}


johnPatient = new Patient("John", 25)
janePatient = new Patient("Jane", 27)
medictf2 = new MEEEDICCC("Herbert Ludwig", 35, "Mercenary", "24/7, even when he sleeps")
hospitel = new Ospitel()
hospitel.pateientLitht.push(johnPatient, janePatient)
hospitel.dfodctorLitht.push(medictf2)
hospitel.bwelarghALLPatients()
hospitel.bwelarghALLMuhdicss()
hospitel.bwelarghSurchMuhdicss()
