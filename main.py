import turtle;
import pandas;

screen = turtle.Screen()
screen.title = ("U.S States Game");
image = "blank_states_img.gif";
screen.addshape(image);
turtle.shape(image);




data = pandas.read_csv("50_states.csv");
state_list = data.state.to_list();
guessed_states = [];

#function

def coordinate_getter(answer_state):
    coordinates = data[data.state == f"{answer_state}"];
    x_value = coordinates['x'].values[0]
    y_value = coordinates['y'].values[0]
    return (x_value, y_value);


score = 0;

while len(guessed_states) <= 50:

    answer_state = screen.textinput(title=f"Guess the state {score}/50 states guessed ", prompt="Whats a states name?").title();
    if answer_state == "Exit":
        list_to_learn = {
            "states": []
        }
        for s in state_list:
            if s not in guessed_states:
                list_to_learn["states"].append(s);
        

        print(list_to_learn)
        data_frame = pandas.DataFrame(list_to_learn);
        data_frame.to_csv("States_needed_to_learn.csv");
        break;
    
    if answer_state in state_list:
        guessed_states.append(answer_state);
        t = turtle.Turtle();
        t.hideturtle();
        print("true");
        t.goto(coordinate_getter(answer_state));
        t.write(str(answer_state));
        score += 1;
        print(score);
    else:
        print("false")

#states to learn to csv



screen.exitonclick();