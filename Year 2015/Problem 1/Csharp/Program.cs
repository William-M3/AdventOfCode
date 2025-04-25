using System.IO;

// Reading text file
string? line;
string puzzle = "";

try
{
    StreamReader sr = new StreamReader("../../../../Puzzle.txt");
    line = sr.ReadLine();
    
    while (line != null)
    {
        puzzle = line;
        line = sr.ReadLine();
    }

    sr.Close();
}
catch (Exception e)
{
    Console.WriteLine($"Message: {e.Message}");
}

char[] floorCommands = puzzle.ToCharArray();
int floor = 0;

// Part 1
// foreach (char command in floorCommands)
// {
//     if (command == '(')
//     {
//         floor++;
//     }
//     else
//     {
//         floor--;
//     }
// }
// Console.WriteLine(floor);

int position = 0;

// Part 2
foreach (char command in floorCommands)
{
    if (command == '(')
        floor++;
    else
        floor--;
    position++;

    if (floor == -1)
    {
        Console.WriteLine(position);
        break;
    }
}