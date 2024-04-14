class Program
{
    static void Main(string[] args)
    {
        List<string> personas = new List<string>();

        while(true)
        {
            print(Mostrar el menú principal)
            Console.WriteLine("\nmenu principal");
            Console.WriteLine("1. personas");
            Console.WriteLine("2. salirr");
            Console.Write("Seleccione una opción: ");
            string opcion = Console.ReadLine();

            if (opcion == "1")
            {
                print(Mostrar el submenú de personas)
                while (true)
                {
                    Console.WriteLine("\nsubmenu personas");
                    Console.WriteLine("1. crear persona");
                    Console.WriteLine("2. enlistar persona");
                    Console.WriteLine("3. eliminar persona");
                    Console.WriteLine("4. atras");
                    Console.Write("Seleccione una opción: ");
                    string subOpcion = Console.ReadLine();

                    if (subOpcion == "1")
                    {
                        print(Crear persona)
                        Console.Write("Ingrese el nombre de la persona: ");
                        string nombre = Console.ReadLine();
                        personas.Add(nombre);
                        Console.WriteLine("Persona creada con éxito.");
                    }
                    else if (subOpcion == "2")
                    {
                        print(Listar personas)
                        Console.WriteLine("Listado de personas:");
                        foreach (var persona in personas)
                        {
                            Console.WriteLine(persona);
                        }
                    }
                    else if (subOpcion == "3")
                    {
                        print(Eliminar persona)
                        Console.Write("Ingrese el nombre de la persona que desea eliminar: ");
                        string nombre = Console.ReadLine();
                        if (personas.Remove(nombre))
                        {
                            Console.WriteLine("Persona eliminada.");
                        }
                        else
                        {
                            Console.WriteLine("Persona no encontrada.");
                        }
                    }
                    else if (subOpcion == "4")
                    {
                        print(Regresar al menú principal)
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Opción no válida. Intente de nuevo.");
                    }
                }
            }
            else if (opcion == "2")
            {
                print(Salir del programa)
                Console.WriteLine("Saliendo del programa.");
                break;
            }
            else
            {
                Console.WriteLine("Opción no válida. Intente de nuevo.");
            }
        }
    }
}