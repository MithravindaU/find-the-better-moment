# Find the Better Moment
## 02 — User Journey

### 1. Journey Overview

Find the Better Moment is designed around a shift in how people plan outings.

Traditional planning often begins with a destination:

> **“Where should we go?”**

The intended experience begins with the person and the experience they want:

> **“What kind of experience do we want, and where and when could we have it?”**

The journey therefore moves from **intent → preferences → recommendations → real-world experience → feedback**.

---

## 2. Before Find the Better Moment

Imagine two friends deciding to spend an evening together.

Their first challenge may not be finding a destination. They may have different moods or expectations.

One person might want:
- A calm environment
- A pleasant breeze
- A scenic view
- Less crowd

The other might want:
- Fun
- Adventure
- Activities
- Something different from the usual routine

The planning process can then become a search for a place that satisfies both people.

A possible approach is to:

1. Discuss what each person feels like doing.
2. Search for destinations that might match.
3. Compare different places.
4. Check weather conditions.
5. Check travel time and traffic.
6. Consider crowd levels and atmosphere.
7. Look for activities nearby.
8. Compare the options.
9. Decide whether the destination is worth the trip.

This can involve multiple sources and repeated comparison.

### The underlying friction

The user is not simply searching for a location.

They are trying to find a **compatible experience**.

---

## 3. The Find the Better Moment Journey

The product vision changes the starting point from destination search to experience discovery.

### Step 1: Express the intention

The user starts with an experience rather than a specific destination.

Examples:
- “I want somewhere peaceful.”
- “We want somewhere fun and adventurous.”
- “We have a few hours free.”
- “We want somewhere outdoors this evening.”
- “We want to explore somewhere new.”

### Step 2: Understand individual preferences

Different people can have different ideas of a good outing.

**Person A**
- Calm
- Scenic
- Less crowded
- Pleasant climate

**Person B**
- Fun
- Adventurous
- Activities
- More things to explore

Instead of forcing users to choose one person's preference, the product vision is to identify places where their preferences can coexist.

For example:

> **A calm beach with a pleasant environment where one person can relax while the other can participate in nearby activities.**

This introduces the idea of **preference intersection** rather than simply averaging preferences.

### Step 3: Narrow the possibilities

The system can use relevant real-world signals to reduce a large number of possible choices.

Potential signals include:
- Weather
- Climate
- Humidity
- Wind
- Crowd levels
- Traffic
- Distance
- Travel time
- Safety considerations
- Cost
- Atmosphere
- Available activities
- Nearby destinations

The objective is not to eliminate user choice. It is to reduce the amount of searching required to reach a reasonable decision.

### Step 4: Recommend a place and time

The system can present a small set of promising options instead of making the user compare an overwhelming number of destinations.

A recommendation should explain **why** it was selected.

For example:

> **Recommended: Location A**  
> Expected to have a more comfortable climate during the selected window, with suitable travel conditions and nearby activities that match the group's preferences.

The recommendation should provide supporting information rather than simply presenting an unexplained AI-generated answer.

### Step 5: Let the user make the final decision

Find the Better Moment is intended to assist the decision, not replace it.

The user can:
- Review the recommendation
- Research the destination further
- Compare alternatives
- Consider personal circumstances
- Choose whether the recommendation is worth trying

Real-world conditions and personal preferences cannot always be predicted perfectly.

---

## 4. The Moment of Truth

The recommendation ultimately has to survive contact with reality.

When the user reaches the destination, several things become immediately noticeable.

### Crowd

Does the actual crowd level feel consistent with what was expected?

### Climate

Does the weather actually feel comfortable?

### View

Does the location visually match the experience the user was looking for?

These factors represent an important transition:

> **The product prediction becomes a real-world experience.**

This is where the system can begin learning whether its recommendations are actually useful.

---

## 5. Post-Experience Feedback

A future version could collect lightweight feedback immediately after the outing.

Instead of asking the user to write a long review, the interface could ask:

### What matched your expectations?

- Crowd
- Climate
- View
- Travel
- Atmosphere
- Activities
- Cost

An optional second prompt could capture mismatches:

### What did not match?

- Too crowded
- Weather was different
- Too noisy
- Travel was not worth it
- More expensive than expected
- Other

This creates structured feedback without adding significant friction.

---

## 6. The Personalization Feedback Loop

The long-term product vision is to use these interactions as signals for personalization.

```text
User Preferences
       ↓
Recommendation
       ↓
Real-World Experience
       ↓
User Feedback
       ↓
Updated Preference Profile
       ↓
Future Recommendations
```

For example, if a user repeatedly selects destinations with low crowds, comfortable weather, natural surroundings, and scenic views, those signals could gradually become stronger in their personal preference profile.

This would allow the system to move from generic recommendations toward recommendations that reflect the individual user.

This is a **future product direction**, not functionality claimed to exist in the current prototype.

---

## 7. Designing for Multiple People

A particularly important use case is planning for groups with different preferences.

The goal is not necessarily to find a destination that is exactly average for everyone. Instead, the system could look for **compatible combinations of preferences**.

| Person | Desired experience |
|---|---|
| Person A | Calm, scenic, low crowd, pleasant breeze |
| Person B | Fun, adventurous, activities |
| Recommendation | A peaceful destination with optional activities nearby |

This creates a more useful interpretation of personalization:

> **Find a place where different people can have a good experience at the same time.**

---

## 8. Current Prototype vs. Future Journey

The current prototype represents only the first part of this larger journey.

### Currently implemented

- User provides an origin and destination.
- User provides a preferred time range.
- Real-time information is obtained through external APIs.
- Travel and weather-related information is considered.
- Possible time windows can be compared.
- A better travel window is recommended.

### Future product journey

- Experience-based intent
- Preference onboarding
- Multi-person preference matching
- Destination recommendations
- Crowd and atmosphere intelligence
- Nearby activity recommendations
- Lightweight post-experience feedback
- Learning from user choices
- Personalized future recommendations

The distinction prevents the case study from presenting future concepts as completed functionality.

---

## 9. Key Product Insight

The user journey revealed that the core problem is not simply **finding a destination**.

It is the uncertainty involved in turning an intention into a worthwhile plan.

The product therefore aims to shorten the path from:

> **“We want to do something.”**

to:

> **“This looks like a good option for us, at this time, and it is worth trying.”**

The final measure of success is not whether the user admired the recommendation algorithm.

It is whether the experience made them feel:

> **“That was worth the shot.”**
