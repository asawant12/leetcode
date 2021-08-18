""" Intro: MQTT is a simple messaging protocol where producers publish data to a topic and subscribers receive that data if they listen to a matching topic pattern.
                    
●  topics are simple strings:
  ○  offices435meetings876peoplelaura                                                                     
●  topic patterns are path strings which can contain two types of wildcards "+" (any number of any alphanumeric characters) and "#" (any rest of string)
   ○  A subscriber for topic above may use a pattern like: 
   offices+meetings+peoplelaura
   or
   offices+meetings#
   or
   offices435meetings#
   or even
   offi+es4+tings#
   ○  Note "+" may appear multiple times, but "#" only once and must be last 
   ○ special characters are not allowed, all characters must be alpha numeric so there is no need to build in a way to escape the wildcard characters for use as part of a string
"""

# TOPIC
# offices435meemeetings876peoplelaura

# TOPIC_PATTERN
# offices + meetings +  peoplelaura


""" Task: Given a topic and topic pattern write a function called does_topic_match returning true if the topic matches the pattern and false if it does not.  Also put additional positive and negative assertion test cases in the main function."""





def match_topic_mattern(topic, topic_pattern):
  ends_with_hash = True if topic_pattern[-1] == "#" else False
  topic_pattern = topic_pattern.strip("#")
  tokens = topic_pattern.split("+")
  prev_token_index = 0
  for token in tokens:
    token_index = topic.find(token)
    if token_index < prev_token_index:
      return False
  if not ends_with_hash:
    token_index = topic.find(tokens[-1])
    if (token_index + len(tokens[-1])) != len(topic):
      return False
  return True

for topic_pat in ("offices+meetings#", "officesxyz+meetinggs#","offices435meetings#", "offi+es4+tings#", "offices+meetings+peoplelaura"):
  match = match_topic_mattern("offices435meetings876peoplelaura", topic_pat)
  if match:
    print(f"Matched:{topic_pat}")
  else:
    print(f"Not Matched: {topic_pat}")

# Time Complexity: O(n) where n is number of tokens
