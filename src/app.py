"""
    Easy Azure Streamlit Demo
    Author: Wolf Paulus (wolf@paulus.com)
"""
import random
import streamlit as st
from log import logger

def coin_flip_with_gamble(initial_money, bet_amount, guess):
    money = initial_money
    result = random.choice(['Heads', 'Tails']).lower()

    
    if guess == result:
        money += bet_amount
        x = f"Correct! You won ${bet_amount}.\\\\\\\\ Total money: ${money}"
        yield x
    else:
        money -= bet_amount
        x = f"Wrong! You lost ${bet_amount}.\\\\\\\\ Total money: ${money}"
        yield x

def ui() -> None:
    st.title("Coin Flip Gambling Game")
    initial_money = 100
    st.write("Your Cash is 100$")
    bet_amount = st.number_input("Input the amount you would like to bet: ")
    guess = st.text_input("Please enter Heads Or Tails").lower()
    flip_gamble = coin_flip_with_gamble(initial_money, bet_amount, guess)

    if st.button("Start Gambling"):
        st.write(next(flip_gamble)





if __name__ == "__main__":
    ui()

