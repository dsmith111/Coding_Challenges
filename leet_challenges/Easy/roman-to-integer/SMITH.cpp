class Solution {
public:
    int switchRoman(string num,string lNum){
        if(num == "I"){
                return 1;
        }
        else if(num == "V"){
            return lNum == "I" ? 3 : 5;            
        }
        else if(num == "X"){
            return lNum == "I" ? 8 : 10;            
        }
        else if(num == "L"){
            return lNum == "X" ? 30 : 50;            
        }
        else if(num == "C"){
            return lNum == "X" ? 80 : 100;            
        }
        else if(num == "D"){
            return lNum == "C" ? 300 : 500;            
        }
        else if(num == "M"){
            return lNum == "C" ? 800 : 1000;            
        }
                
        return 0;
    }
    int romanToInt(string s) {

        int count = 0;
        string numeral = "";
        string lNum = "";
        
        for(int i = 0; i < s.length(); i++){
            numeral = s[i];
            count += switchRoman(numeral, lNum);
            lNum = numeral;
        }
        return count;
    }
};