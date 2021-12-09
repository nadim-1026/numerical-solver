print("select subject")
print("1. fluid mechanics")
print("2.kinematic machinary analytical analysis")
print("3.unit coversion")
print("4: NSM")

while True:
    choice=input("enter your choice(1/2/3/4):")
    if choice== "1":
        print("1.characteritics of fluid")
        print("2.height of capillary")
        print("3.simple manometer")
        print("4.differential manometer")
        while True:
            choice = input("enter your choice(1/2/3/4):")
            if choice=="1":
                weight = int(input("enter the weight in KN:"))
                volume = int(input("enter the volume in m^3:"))
                weightdensity = weight / volume
                specificdensity = weightdensity / 9.81
                specificvolume = 1 / specificdensity
                specificgravity = specificdensity / 1000
                print(weight)
                print(volume)
                print("weight density is given by :", weightdensity)
                print("specific density is given by:", specificdensity)
                print("specific volume is given by:", specificvolume)
                print("specific gravity is given by:", specificgravity)
            elif choice=="2":
                import math

                surfacetension = int(input("enter surface tension:"))
                a = int(input("enter angle of contact:"))
                density = int(input("enter density of liquid:"))
                diameter = int(input("diameter of capilary"))
                cosine_a = math.cos(math.radians(a))
                h = (4 * surfacetension * cosine_a) / (density * diameter * 9.81)
                print("height of the liquid coloumn is:", h)

            elif choice=="3":
                print("1.pizomanometer")
                print("2.u-tube manometer")
                while True:
                    choice = input("enter your choice(1/2/):")
                    if choice == "1":
                        print("all the value should be in S.I. unit")
                        h1 = float(input("enter the height of fluid or reading 1:"))
                        h2 = float(input("enter the height of fluid or reading 2:"))
                        q = float(input("density of fluid:"))
                        h_avg = (h1 + h2) / 2
                        print("average height of fluid:", h_avg)

                        p = q * 9.81 * h_avg
                        print("pressure at point is:", p, "pascal")
                    elif choice == "2":
                        print("all the value should be in S.I. unit")
                        h1 = float(input("enter the height of fluid or reading 1:"))
                        h2 = float(input("enter the height of fluid or reading 2:"))
                        h3 = float(input("enter the height of manometric fluid , reading 1:"))
                        h4 = float(input("enter the height of manometric fluid or reading 2:"))
                        q1 = float(input("density of fluid:"))
                        q2 = float(input("density of manometric fluid:"))
                        H1 = (h1 + h2) / 2
                        H2 = (h3 + h4) / 2
                        P1 = (q2 * 9.81 * H2) - (q1 * 9.81 * H1) - 101300
                        P = (q2 * 9.81 * H2) - (q1 * 9.81 * H1)
                        print("average height of fluid:", H1)
                        print("average height of monometric fluid:", H2)
                        print("absolute pressure at p:", P1, "pascal")
                        print(" guage pressure at point p:", P, "pascal")


            elif choice=="4":
                print("1.u-tube differential manometer")
                print("2.inverted u-tube differential manometer")

                while True:
                    choice = input("enter your choice(1/2/):")
                    if choice == "1":
                        print("all the value should be in S.I. unit")
                        h1 = float(input("enter the height of fluid  in left limb :"))
                        h2 = float(input("enter the height of manometric fluid in right limb:"))
                        h3 = float(input("enter the height of fluid  in right limb:"))
                        q1 = float(input("density of fluid in left limb:"))
                        q2 = float(input("density of manometric fluid:"))
                        q3 = float(input("density of fluid in right limb:"))
                        print(
                            "according to pascal law pressure at left limb above x-axis is equal to pressure at right limb")
                        print(h1)
                        print(h2)
                        print(h3)
                        print(q1)
                        print(q2)
                        print(q3)

                        Pab = ((q2 * 9.81 * h2) + (q3 * 9.81 * h3)) - (q1 * 9.81 * h1)

                        print("pressure difference between two points is:", Pab, "pascal")

                    elif choice == "2":
                        print("all the value should be in S.I. unit")
                        h1 = float(input("enter the height of fluid  in left limb :"))
                        h2 = float(input("enter the height of manometric fluid in right limb:"))
                        h3 = float(input("enter the height of fluid  in right limb:"))
                        q1 = float(input("density of fluid in left limb:"))
                        q2 = float(input("density of manometric fluid:"))
                        q3 = float(input("density of fluid in right limb:"))
                        print(
                            "according to pascal law pressure at left limb below x-axis is equal to pressure at right limb")
                        print(h1)
                        print(h2)
                        print(h3)
                        print(q1)
                        print(q2)
                        print(q3)

                        Pab = ((q2 * 9.81 * h2) + (q3 * 9.81 * h3)) - (q1 * 9.81 * h1)

                        print("pressure difference between two points is:", Pab, "pascal")

    elif choice=='2':
        print("1.slider crank mechanism")
        print("2.degrre of freedom")
        print("3.single hooke's joint")
        print("4..double hooke's joint")


        while True:
            choice = input("enter your choice(1/2/3/4):")
            if choice=='1':
                r = float(input("length of crank r="))
                l = float(input("length of connecting rod l= "))
                speedofcrank = int(input("speed of crank in RPM:"))
                aa = float(input("enter the angular accelration of crank:"))
                O = float(input("angle by crank: "))
                n = l / r
                avc = (2 * 3.14 * speedofcrank) / 60

                print("obliquity ratio is :", n)
                print("angular velocity of crank:", avc)


                import math

                sine_O = math.sin(math.radians(O))
                cosine_O = math.cos(math.radians(O))
                xp = r * (1 - cosine_O) + r * (n - math.sqrt(n * n - sine_O * sine_O))
                print("displacement of piston is:", xp)
                vp = r * avc * ( (sine_O )  + (2 * sine_O * cosine_O) / (2 * n))

                print(sine_O)
                print(cosine_O)
                print("velocity of a piston is:", vp)

                ap1 = (avc * avc * r * (cosine_O + (cosine_O * cosine_O - sine_O * sine_O) / (n)))  # if velocity of crank is uniform
                ap2 = (avc * avc * r * (cosine_O + (cosine_O * cosine_O - sine_O * sine_O) / (n))) + vp  # if velocity of crank is not uniform


                print("angular accelration of a piston with uniform speed:", ap1)
                print("angular accelration of a piston with not uniform speed:", ap2)
                avcr = (avc * cosine_O) / n
                print("angular velocity of connecting rod is:", avcr)
                aacr1 = -(avc * avc * sine_O) / n  # if angular velocity of crank is uniform
                aacr2 = -(avc * avc * sine_O) / n + ((aa * cosine_O) / n)  # if angular velocity of crank is not uniform

                print("angular accelaration of connecting rod with unifom speed:", aacr1)
                print("angular accelaration of connecting rod with not  unifom speed:", aacr2)

            elif choice=='2':
                l = int(input("enter number of link"))
                j = int(input("enter number of joint"))
                h = int(input("enter number of higher pair"))
                n = (3 * (l - 1) - 2 * j - h)
                print("number of degree of freedom:", n)
                if n == 0:
                    print("mechanism forms a stracture")
                elif n == 1:
                    print("mechanism is incompletely constarin")
                elif n == 2:
                    print("mechanism is completely constarin")
                elif n == -1:
                    print("mechanism shows staticaly indeterminate structure")

            elif choice=="3":
                import math

                n = int(input("enter the speed of driving shaft:"))
                g = int(input("enter angle made by driving shaft:"))
                k = int(input("enter angle between driving shaft and driven shaft:"))
                w = (2 * 3.14 * n / 60)
                sine_k = math.sin(math.radians(k))
                cosine_g = math.cos((math.radians(g)))
                cosine_k = math.cos(math.radians(k))
                print(sine_k)
                print(cosine_k)
                print(cosine_g)
                wd = (w * (cosine_k) / (1 - cosine_g * cosine_g * sine_k * sine_k))
                dsmax = n / cosine_k
                dsmin = n * cosine_k

                print("angular velocity of driving shaft is:", w)
                print("angular velocity of driven shaft:", wd)
                print("maximum speed of driven shaft:", dsmax)
                print("minimum speed of driven shaft:", dsmin)

            elif choice=='4':
                import math

                n = int(input("enter the speed of driving shaft"))
                k = int(input("enter angle between driving shaft and driven shaft:"))
                cosine_k = math.cos(math.radians(k))
                intmax = n / cosine_k
                intmin = n * cosine_k
                dsmax = intmax / cosine_k
                dsmin = intmin * cosine_k
                print("maximum speed of intermidiate shaft:", intmax)
                print("minimum speed of intermidiate shaft:", intmin)
                print("maximum speed of driving shaft shaft:", dsmax)
                print("minimum speed of driving shaft shaft:", dsmin)

    elif choice=='3':
        num1 = input('Enter the value: ')
        unit1 = input('Which unit do you want it converted from:  ')
        unit2 = input( 'Which unit do you want it converted to: ')

        if unit1 == "cm" and unit2 == "m":
            ans = float(num1) / 100
            print(ans)
        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1) / 10
            print(ans)
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1) * 100
            print(ans)
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1) * 10
            print(ans)
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1) / 1000
            print(ans)
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1) * 1000
            print(ans)
        elif unit1 == "km" and unit2 == "m":
            ans = float(num1) * 1000
            print(ans)
        elif unit1 == "m" and unit2 == "km":
            ans = float(num1) / 1000
            print(ans)
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1) / 1000000
            print(ans)
        elif unit1 == "ft" and unit2 == "cm":
            ans = float(num1) * 30.48
            print(ans)
        elif unit1 == "ft" and unit2 == "mm":
            ans = float(num1) * 304.8
            print(ans)
        elif unit1 == "ft" and unit2 == "inch":


            ans = float(num1) * 12
            print(ans)
        elif unit1 == "inch" and unit2 == "cm":
            ans = float(num1) ** 54
        elif unit1 == "inch" and unit2 == "mm":
            ans = float(num1) * 25.4
        elif unit1 == "bar" and unit2 == "N/m*m":
            ans = float(num1) * 10 ** 5
            print(ans)
        elif unit1 == "N/m*m" and unit2 == "bar":
            ans = float(num1) / 10 ** 5
            print(ans)



    elif choice=='4':
        print("1.bisection method if error is given")
        print("2.bisection method if no of iteration is given is ")
        print("3.regula falsi method")
        print("4newton raphsion method")
        print("5:euler method ")
        print("6 R.K 2nd order method")
        print("7:R.K 4th order method")

        while True:
            choice = input("enter your choice(1/2/3/4/5/6/7):")
            if choice == '1':
                def f(x):
                    y = 2 * x ** 3 + 4 * x ** 2 - 8
                    return y


                def bisection(a, b, n):
                    i = 0
                    for i in range(n):
                        x = (a + b) / 2
                        if f(x) > 0:
                            a = x
                        else:
                            b = x

                        print("itteration:", i, 'X=', x, 'f(x)=', f(x))
                        if i == n:
                            break
                        else:
                            i = i + 1

                    print("root of the equation", x)


                a = float(input("enter first initial guess:"))
                b = float(input("enter second initial guess:"))
                n = int(input("enter the no of itteration"))

                print(f(a))
                print(f(b))

                if f(a) * f(b) > 0:
                    print(" equation doesnt belongs to the bi section method")
                else:
                    bisection(a, b, n)
            elif choice == '2':
                import math


                def f(x):
                    y = math.cos(x) - 1.3 * x
                    return y


                a = float(input("enter first initial guess:"))
                b = float(input("enter second initial guess:"))
                e = float(input("enter the error"))

                print(f(a))
                print(f(b))

                if f(a) * f(b) > 0:
                    print(" equation doesnt belongs to the bi section method")
                else:
                    i = 0
                    while (abs(b - a) > e):
                        x = (a + b) / 2
                        if f(x) > 0:
                            a = x
                        else:
                            b = x
                        i = i + 1

                        print(i, x, f(x))

                    x = (a + b) / 2
                    print("root of the equation:", x)

            elif choice == '3':
                import math


                def f(x):
                    y = math.exp(x) * math.cos(x) - 1.2 * math.sin(x) - 0.5
                    return y


                a = float(input("enter first initial guess:"))
                b = float(input("enter second initial guess:"))
                n = int(input("enter the no of itteration"))

                print(f(a))
                print(f(b))

                if f(a) * f(b) > 0:
                    print(" equation doesnt belongs to the false position method")
                else:
                    i = 0
                    for i in range(n):
                        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
                        if f(x) > 0:
                            a = x
                        else:
                            b = x

                        print("itteration:", i, 'X=', x, 'f(x)=', f(x))
                        if i == n:
                            break
                        else:
                            i = i + 1

                    print("root of the equation", x)

            elif choice == '4':
                def f(x):
                    y = math.exp(x) * math.cos(x) - 1.4
                    return y


                def df(x):
                    y = -math.exp(x) * math.sin(x) + math.exp(x) * math.cos(x)
                    return y


                def ddf(x):
                    y = -(2 * math.exp(x) * math.sin(x))
                    return y


                x1 = int(input("take initial guess"))
                n = int(input("no of itt:"))
                y1 = f(x1)
                y2 = df(x1)
                y3 = ddf(x1)
                print(y1, "\n", y2, "\n", y3)

                if ((y1 * y3) / y2 ** 2) > 1:
                    print("numerical dosesnt belongs to newton rapshen method")
                else:
                    i = 0
                    for i in range(n):
                        x2 = x1 - (f(x1) / df(x1))
                        x1 = x2
                        print("no of iteration=", i, "x2=", x2)

                    print("root of the equation", x1, "at no of iteration", i)





            elif choice == '5':
                def f(x, y):
                    y = x - y ** 2
                    return y


                xo = float(input("enter initial value of x0:"))
                yo = int(input("enter initial value of y0 :"))
                xg = float(input("enter the given value of xg:"))
                h = float(input("enter step size:"))

                n = (xg - xo) / h

                for i in range(int(n)):
                    yg = yo + h * f(xo, yo)
                    xo = xo + h
                    yo = yg
                    print("no of itteration=", i, "yg=", yg)

                print("the final value of yg", yg)

            elif choice == '6':
                def f(x, y):
                    y = (y ** 2 - x ** 2) / (y ** 2 + x ** 2)
                    return y


                xo = int(input("enter initial value of x0:"))
                yo = int(input("enter initial value of y0 :"))
                xg = float(input("enter the given value of xg:"))
                h = float(input("enter step size:"))

                n = (xg - xo) / h
                for i in range(int(n)):
                    k1 = h * f(xo, yo)
                    k2 = h * f(xo + h, yo + k1)
                    k = (k1 + k2) / 2
                    yg = yo + k
                    xo = xo + h
                    yo = yg
                    print("no of itteration=", i, "k1=", k1, "k2=", k2, "k=", k, "yg=", yg)

                print("the final value at xg", yg)

            elif choice == '7':
                def f(x, y):
                    y = x * y + y ** 2
                    return y


                xo = int(input("enter initial value of x0:"))
                yo = int(input("enter initial value of y0 :"))
                xg = float(input("enter the given value of xg:"))
                h = float(input("enter step size:"))

                n = (xg - xo) / h
                print("n=", n)
                for i in range(int(n)):
                    k1 = h * f(xo, yo)
                    k2 = h * f(xo + (h / 2), yo + (k1 / 2))
                    k3 = h * f(xo + (h / 2), yo + (k2 / 2))
                    k4 = h * f(xo + h, yo + k3)
                    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
                    yg = yo + k
                    xo = xo + h
                    yo = yg
                    print("no of iterattion", i, "k1=", k1, "k2=", k2, "k3=", k3, "k4=", k4, "k=", k, "yg=", yg)

                print("the final value at xg", yg)











    else:
        print("invalid")




