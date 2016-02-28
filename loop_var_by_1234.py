__name__ = "vutsuak"

# the sole aim of this program is to check the time complexity when the loop variable is incremented by 1,2,3,4. Til it is greater than n

n = 100

i = 0
j = 1
while i < n:
    i = i + j
    print i
    j += 1


# since i is taking the natural number series format it is incresing its value at every step and the progresion is i*(i+1)/2<n
# the complexity is theta(sqrt(n))
