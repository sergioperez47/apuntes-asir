cadena_1 = "hola"
cadena_2 = ('Hola')

print(cadena_2 == cadena_1)

print(cadena_1 + "\n"+ cadena_2)

print(r"rico \n rico \ fundamento")

cadena_larga= '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ut lacus magna. 
    Fusce luctus in enim ac maximus. Curabitur dignissim enim et cursus vestibulum. 
    Pellentesque vestibulum faucibus lacus, et ultricies nibh condimentum eget. 
    Pellentesque venenatis malesuada aliquam. Vestibulum consectetur porta neque at consectetur. 
    Nulla imperdiet volutpat lectus, eu placerat massa. 
    Integer convallis semper aliquam. Curabitur euismod scelerisque porttitor. 
    Mauris iaculis gravida tincidunt. Aliquam vitae eros nunc. 
    Donec dictum tellus ac erat porttitor pulvinar. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
    Suspendisse venenatis in nisl vitae ultrices. Ut fermentum felis eu varius gravida.

    Proin eget libero a mauris tincidunt lobortis. 
    Donec eu tristique arcu, et pellentesque purus. 
    Donec vulputate nibh nec nulla ultricies, a scelerisque velit interdum. 
    Morbi sed magna ut augue mattis viverra. 
    Nullam rutrum nisi at lorem sagittis auctor. 
    Aenean eget aliquam massa. 
    Phasellus hendrerit viverra turpis id hendrerit. 
    Proin congue at turpis in iaculis. 
    Suspendisse ac tellus et quam efficitur fermentum. 
    Maecenas diam augue, rutrum sed sapien vitae, fermentum cursus mauris. 
    Quisque eu molestie risus. Vestibulum ullamcorper arcu et dui mattis ultricies. 
    Vestibulum quis tincidunt libero.
'''
print(cadena_larga)

print(cadena_1*2)

print(cadena_2*len(cadena_1))

print(cadena_1[1])
print(cadena_1[0])
print(cadena_1[-1])
print(cadena_larga[5])
print(cadena_larga[14:21])
print(cadena_larga[:31])