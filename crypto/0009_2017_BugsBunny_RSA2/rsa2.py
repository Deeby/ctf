import fractions
from Crypto.Util.number import long_to_bytes

def continued_fractions(n, e):
    cf = [0]
    while e != 0:
        cf.append(int(n/e))
        N = n
        n = e
        e = N % e
    return cf

def calcKD(cf):
    kd = list()
    for i in range(1, len(cf)+1):
        tmp = fractions.Fraction(0)
        for j in cf[1:i][::-1]:
            tmp = 1 / (tmp+j)
        kd.append((tmp.numerator, tmp.denominator))
    return kd

def calcPQ(a, b):
    if a*a < 4*b or a < 0:
        return None
    c = int_sqrt(a*a-4*b)
    p = (a + c) / 2
    q = (a - c) / 2

    if p + q == a and p * q == b:
        return (p, q)
    else:
        return None

def int_sqrt(n):
    def f(prev):
        while True:
            m = (prev + n/prev) / 2
            if m >= prev:
                return prev
            prev = m
    return f(n)

def wiener(n, e):
    kd = calcKD(continued_fractions(n, e))
    for (k, d) in kd:
        if k == 0:
            continue

        if (e*d-1) % k != 0:
            continue

        phin = (e*d-1) / k
        if phin >= n:
            continue

        ans = calcPQ(n-phin+1, n)
        if ans is None:
            continue

        return (ans[0], ans[1])

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return x

c = 0x217c8bf9b45601267624c3b1ba89ae93d04c8fae32dc15496262f36f48d06c0dc9e178a77b77a33708dcbe1fcd55ea9eb636fe5684c2f0f08df3389f47b36a128636671eba300491c829ed1e252b1bb4dbb3b93bc46d98a10bb5d55347752052ab45e143fd46799be1d06ac3ff7e8b1eb181dfbba8dfac3910202fd0b9a25befe
e = 266524484526673326121255015126836087453426858655909092116029065652649301962338744664679734617977550306567819672969837450223062478394149960243362563995235387971047857994699247277712682103161537347874310994510059329875060868679654080020041070975648626636209785889112656335054840517934593236597457100751820027783
n = 412460203584740978970185080155274765823237615982150661072746604041385717906706098256415230390148737678989448404730885157667896599397615737297545930957425615121654272472589331747646564634264520011009284080299605233265170506809736069720838542498970453928922703911186788239628906189362646418960560442406497717567

(p, q) = wiener(n, e)
# p = 24033342257638708824373735251516351694011297880096219691762845250861823504037151195236378659607369447498245214333469418187337738705973799517129078918392601
# q = 17161999324236539064317754140395642765702739382246098180731387908161141783840551460502918960425597679930951305598922767957529406215641102387965223811833367

phi = (p-1) * (q-1)
d = egcd(e, phi)
print long_to_bytes(pow(c, d, n))