import sys
mongendata = [[],[],[],[],[],[],[],[],[],[]]
montypedata = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
mongensizes = {
    0: 898,
    1: 151,
    2: 100,
    3: 135,
    4: 107,
    5: 156,
    6: 72,
    7: 88,
    8: 89
}
montypesizes = {
    "b": 86,
    "k": 69,
    "d": 63,
    "e": 65,
    "y": 61,
    "h": 68,
    "f": 78,
    "l": 110,
    "t": 60,
    "g": 111,
    "o": 74,
    "i": 54,
    "n": 119
}
def getdata():
    directory = 'Data Files/'
    store = open(directory + 'allalphapy.txt','r');
    content = store.read()
    mongendata[0] = content.splitlines()
    store = open(directory + 'gen1alphapy.txt','r');
    content = store.read()
    mongendata[1] = content.splitlines()
    store = open(directory + 'gen2alphapy.txt','r');
    content = store.read()
    mongendata[2] = content.splitlines()
    store = open(directory + 'gen3alphapy.txt','r');
    content = store.read()
    mongendata[3] = content.splitlines()
    store = open(directory + 'gen4alphapy.txt','r');
    content = store.read()
    mongendata[4] = content.splitlines()
    store = open(directory + 'gen5alphapy.txt','r');
    content = store.read()
    mongendata[5] = content.splitlines()
    store = open(directory + 'gen6alphapy.txt','r');
    content = store.read()
    mongendata[6] = content.splitlines()
    store = open(directory + 'gen7alphapy.txt','r');
    content = store.read()
    mongendata[7] = content.splitlines()
    store = open(directory + 'gen8alphapy.txt','r');
    content = store.read()
    mongendata[8] = content.splitlines()
    store = open(directory + 'bugmonalphapy.txt','r');
    content = store.read()
    montypedata[0] = content.splitlines()
    store = open(directory + 'darkmonalphapy.txt','r');
    content = store.read()
    montypedata[1] = content.splitlines()
    store = open(directory + 'dragonmonalphapy.txt','r');
    content = store.read()
    montypedata[2] = content.splitlines()
    store = open(directory + 'electricmonalphapy.txt','r');
    content = store.read()
    montypedata[3] = content.splitlines()
    store = open(directory + 'fairymonalphapy.txt','r');
    content = store.read()
    montypedata[4] = content.splitlines()
    store = open(directory + 'fightingmonalphapy.txt','r');
    content = store.read()
    montypedata[5] = content.splitlines()
    store = open(directory + 'firemonalphapy.txt','r');
    content = store.read()
    montypedata[6] = content.splitlines()
    store = open(directory + 'allwords.txt','r');
    content = store.read()
    mongendata[9] = content.splitlines()

def checkdata():
    for i in range (1,9):
        for j in range(mongensizes[i]):
            if not(mongendata[i][j] in mongendata[0]):
                print(mongendata[i][j]+"is not in the list of all pokemon\n")

def port(a, b):
    longest = 0
    if len(a) < len(b):
        smollest = (0,len(a))
    elif len(a) > len(b):
        smollest = (1,len(b))
    else:
        smollest = (2,len(a))
    a = a.lower()
    b = b.lower()

    for i in range(1,smollest[1]+1):
        end = a[len(a)-i:len(a)]
        start = b[0:i]
        if end == start:
            longest = i
    #std::cout << a << " ? " << b << " ? " << longest << "\n";
    if longest < 2:
        return False;
    else:
        return True;

def dupSearch(a, b):
    none = True
    if a in b:
        none = False
    if b in a:
        none = False
    return none;

def findports(a, b, prints):
    portlist = []
    for i in range(len(a)):
        for j in range(len(b)):
            if port(a[i],b[j]):
                if dupSearch(a[i],b[j]):
                    if prints:
                        ports = a[i] + ", " + b[j]
                        print(ports)
                        portlist.append(ports)
                    else:
                        ports = a[i] + ", " + b[j]
                        portlist.append(ports)
    return portlist

#findports(montypedata[0],montypedata[1],True)
getdata()
checkdata()
print("Welcome to Make a Port!")
print("What will be your first port? 0 for all pokemon, the gen number (1-8) for all pokemon of that gen, or 9 for all English words.")
ans = input()
try:
    ans = int(ans)
except:
    print("That's not a valid value")
    sys.exit()
if ans < 10 and ans > -1:
    ports = mongendata[ans]
else:
    print("That's not a valid value")
    sys.exit()
for i in range(len(ports)):
    print(ports[i])
while not ans == -1:
    print("What is your next port? -1 to stop, 0 for all pokemon, the gen number (1-8) for all pokemon of that gen, or 9 for all English words.")
    ans = input()
    try:
        ans = int(ans)
    except:
        print("That's not a valid value")
        sys.exit()
    if ans < 10 and ans > -1:
        ports = findports(ports,mongendata[ans],True)
    elif ans == -1:
        print("Thanks for your stay.")
        sys.exit()
    else:
        print("That's not a valid value")

        sys.exit()
    if len(ports) == 0:
        print("There doesn't appear to be any more valid ports. Therefore, the program has ended.")
        sys.exit()
#store = open('gen9alphapy.txt','w')
#store.write("""""")
#store.close()
'''
std::vector<std::string> l;
std::vector<std::vector<std::string>> mongendata = {{},{},{},{},{},{},{},{},{}};
std::map<int,int> mongensizes = {{0,898},{1,151},{2,100},{3,135},{4,107},{5,156},{6,72},{7,88},{8,89}};
void getdata(){
    std::string line;
    std::ifstream allalpha ("allalpha.txt");
    for (int i = 0; i < 898; i++){
        getline(allalpha,line);
        //a.push_back(line);
        mongendata[0].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen1alpha ("gen1alpha.txt");
    for (int i = 0; i < 151; i++){
        getline(gen1alpha,line);
        //b.push_back(line);
        mongendata[1].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen2alpha ("gen2alpha.txt");
    for (int i = 0; i < 100; i++){
        getline(gen2alpha,line);
        //c.push_back(line);
        mongendata[2].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen3alpha ("gen3alpha.txt");
    for (int i = 0; i < 135; i++){
        getline(gen3alpha,line);
        //d.push_back(line);
        mongendata[3].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen4alpha ("gen4alpha.txt");
    for (int i = 0; i < 107; i++){
        getline(gen4alpha,line);
        //e.push_back(line);
        mongendata[4].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen5alpha ("gen5alpha.txt");
    for (int i = 0; i < 156; i++){
        getline(gen5alpha,line);
        //f.push_back(line);
        mongendata[5].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen6alpha ("gen6alpha.txt");
    for (int i = 0; i < 72; i++){
        getline(gen6alpha,line);
        //g.push_back(line);
        mongendata[6].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen7alpha ("gen7alpha.txt");
    for (int i = 0; i < 88; i++){
        getline(gen7alpha,line);
        //h.push_back(line);
        mongendata[7].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream gen8alpha ("gen8alpha.txt");
    for (int i = 0; i < 89; i++){
        getline(gen8alpha,line);
        //k.push_back(line);
        mongendata[8].push_back(line);
        //std::cout << line << "\n";
    }
    std::ifstream alltwoalpha ("alltwoalpha.txt");
    for (int i = 0; i < 3070; i++){
        getline(alltwoalpha,line);
        l.push_back(line);
        //std::cout << line << "\n";
    }
}
void checkdata(){
    for (int i = 1; i < 9; i++){
        for (int j = 0; j < mongensizes.at(i); j++){
            if (std::find(mongendata[0].begin(),mongendata[0].end(),mongendata[i][j]) == mongendata[0].end()) {
                std::cout << mongendata[i][j] << "is not in the list of all pokemon\n";
            }
        }
    }
}

void portchain(int len, std::vector<std::string> a, std::vector<std::string> b){
    if (len == 3) {
        findports(a,b,true);
    }
    else {
        std::vector<std::string> portlist = findports(a,b,false);
        portchain(len - 1, portlist,b);
    }
}

int main(int argc, const char * argv[]) {
    std::vector<std::string> ports;
    int ans = -2;
    getdata();
    checkdata();
    std::cout << "Welcome to Make a Port!\n";
    std::cout << "What will be your first port? 0 for all pokemon, or the gen number (1-8) for all pokemon of that gen.";
    std::cin >> ans;
    if (ans < 9 && ans > -1) {
        ports = mongendata[ans];
    }
    else {
        std::cout << "That's not a valid value\n";
        fclose(stdin);
        return(0);
    }
    for(int i = 0; i < ports.size(); i++){
        std::cout << ports[i] << "\n";
    }
    while (ans != -1){
        std::cout << "What is your next port? -1 to stop, 0 for all pokemon, or the gen number (1-8) for all pokemon of that gen.";
        std::cin >> ans;
        if (ans < 9 && ans > -1) {
            ports = findports(ports,mongendata[ans],true);
        }
        else if (ans == -1) {
            std::cout << "Thanks for your stay.\n";
            fclose(stdin);
            return(0);
        }
        else {
            std::cout << "That's not a valid value\n";
            fclose(stdin);
            return(0);
        }
        if (ports.size() == 0){
            std::cout << "There doesn't appear to be any more valid ports. Therefore, the program has ended.\n";
            return(0);
        }
    }
    std::cout << "There's a bug!\n";
    fclose(stdin);
    //input code
    /*std::string line;
    std::vector<std::string> a;
    freopen("gen9alpha.txt","w",stdout);*/
    //input testing code
    /*std::string line;
    freopen("gen9alpha.txt","r", stdin);
    for (int i = 0; i < 151; i++){
        std::cin >> line;
        std::cout << line << "\n";
    }*/
}
'''
