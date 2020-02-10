function isPositive(a) {
    for (i = 0; i < a; i++){
        
        try{
        if (a<0){
            throw "Negative Error"
        } else
            if (a == 0){
                throw "Zero Error";
            } else {
                return "YES"
            } 
            
        }  catch(err){
            return err;
        }  
        
    }
}

console.log(isPositive(-1))