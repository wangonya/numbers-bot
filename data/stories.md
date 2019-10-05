## fallback story
* out_of_scope
  - action_default_fallback

## story_001
* greet
  - utter_greet
* get_number_fact
  - get_number_fact

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* get_number_fact{"number": "21"}
    - slot{"number": "21"}
    - get_number_fact
* get_number_fact{"number": "13"}
    - slot{"number": "13"}
    - get_number_fact
* bot_challenge

## interactive_story_1
* greet
    - utter_greet
* get_number_fact{"number": "64"}
    - slot{"number": "64"}
    - get_number_fact
* get_number_fact{"number": "92"}
    - slot{"number": "92"}
    - get_number_fact
* bot_challenge
* get_number_fact{"number": "54"}
    - slot{"number": "54"}
    - get_number_fact
* get_number_fact{"number": "1"}
    - slot{"number": "1"}
    - get_number_fact

## New Story

* greet
    - utter_greet
* get_number_fact{"number":"21"}
    - slot{"number": "21"}
    - get_number_fact
* get_number_fact{"number":"32"}
    - slot{"number": "32"}
    - get_number_fact
* get_number_fact{"number":"63"}
    - slot{"number": "63"}
    - get_number_fact
* get_number_fact{"number":"43"}
    - slot{"number": "43"}
    - get_number_fact
* get_number_fact{"number":"0"}
    - slot{"number": "0"}
    - get_number_fact
* bot_challenge
    - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* get_number_fact{"number": "66"}
    - slot{"number": "66"}
    - get_number_fact
* get_number_fact{"number": "99"}
    - slot{"number": "99"}
    - get_number_fact
* get_number_fact{"number": "0"}
    - slot{"number": "0"}
    - get_number_fact

## New Story

* greet
    - utter_greet
* get_number_fact{"number":"89"}
    - slot{"number":"89"}
    - get_number_fact
* get_number_fact{"number":"332"}
    - slot{"number":"332"}
    - get_number_fact
* get_number_fact{"number":"32"}
    - slot{"number":"32"}
    - get_number_fact

## New Story

* greet
    - utter_greet
* get_number_fact{"number":"54"}
    - slot{"number":"54"}
    - get_number_fact
* get_number_fact{"number":"12"}
    - slot{"number":"12"}
    - get_number_fact
* get_number_fact{"number":"00"}
    - slot{"number":"00"}
    - get_number_fact
* get_number_fact{"number":"543"}
    - slot{"number":"543"}
    - get_number_fact
* get_number_fact{"number":"2"}
    - slot{"number":"2"}
    - get_number_fact

## interactive_story_1
* greet
    - utter_greet

## New Story

* greet
    - utter_greet
* goodbye
    - action_default_fallback
* out_of_scope
    - action_default_fallback
* null
    - action_default_fallback
* get_number_fact{"number":"32"}
    - slot{"number":"32"}
    - get_number_fact
* get_number_fact{"number":"101"}
    - slot{"number":"101"}
    - get_number_fact
* get_number_fact{"number":"11"}
    - slot{"number":"11"}
    - get_number_fact
* get_number_fact{"number":"10"}
    - slot{"number":"10"}
    - get_number_fact
