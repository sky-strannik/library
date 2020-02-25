// ToUpper всех символов на латинице
string s = "1234aSdццц457";
string result = string.Empty;
 
for (int i=0; i<s.Length; i++)
{
    if (s[i]>='a' && s[i]<='z')
        result += s[i].ToString().ToUpper();
    else result += s[i].ToString();
}
 
return result;