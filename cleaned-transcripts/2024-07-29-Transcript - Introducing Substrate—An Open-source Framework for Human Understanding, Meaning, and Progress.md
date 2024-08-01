Alright, welcome to Unsupervised Learning. This is Daniel Miser, and today I'm super excited to announce a project that I've been wanting to talk about for a long time - called Substrate.

So what exactly is Substrate? It's an open-source framework designed for human understanding, meaning, and progress. You might be wondering "What does that even mean?" That’s a great question!

The main purpose of this project is to make things that matter to humans more transparent and discussable, so they can ultimately become more fixable because they're transparent and discussable.

When we talk about understanding meaning and progress, these are the components we're referring to. We call them Substrate components - collections of ideas like a list of human novel ideas, problems (a list of our most important human issues), beliefs, models which represent ways of conceptualizing reality, frames (lists of narratives or lenses for perceiving reality), solutions that correspond to those problems, information sources (like The New York Times, The Hill, Breitbart etc.), government sources, individual sources, different media organizations and must span various political ideologies. It's also essential to include comprehensive laws (starting with the US Government but expanding worldwide) and claims about facts or truths in the world.

In addition, we have votes related to laws submitted for approval, arguments that are made either in favor of or against a particular issue, funding sources from lobbyists along with their agendas, missions, goals, and verified facts. The structure allows anyone in the open-source community - worldwide contributors - to add problems, claims, information sources, goals, etc., all within repositories maintained on GitHub.

We already have started collecting some of these components, for example, we've got a list of issues such as Ransomware attacks on healthcare systems, teen depression in the UK, and nuclear weapons development in North Korea. Each issue has a unique code to link it directly, allowing easy tracking and updating.

The Substrate project is designed to provide a handle on topics that are often challenging to discuss effectively. The main goal is to articulate these things better among ourselves and with others. 

Let's delve into an example of the Argument component. Consider a common argument about recycling: "I don't see why you recycle, it costs too much and the programs aren't well-run." This type of argument is turned into something more structured:

1. **Effort Required** - Cost to implement
2. **Cost of Progress** - Benefits for environmental impact

This breakdown helps in understanding the different aspects contributing to an argument, making it easier to discuss and evaluate.
Then, it breaks those into further things: recycling programs require significant effort, recycling programs are expensive, most rejected materials end up in landfills. Okay, okay, and then it goes and adds research to all of those; in this case, it was pulled directly out of the model but you can actually add AI on top of this which we're going to be doing with an agent framework either that we build ourselves or that we use one of the third parties. These will actually be tools doing this research down here. Okay, going and doing separate lookups to find research like you could do this at a really in-depth level for each stage here, especially this one where you're doing the research, and then it comes back and says supports, weakens, or partially supports. Then we have a conclusion that ends up being a weak argument; interesting! So, you could see the reasons this is the most important thing, you could see how this argument was formed, how it was researched using what sources.

Look at this, uh, recycling statistics 2021 National waste and recycling Association 2022. So we actually have Source names here, and we can go into even more depth if we want to add content from other sources. Boom! You start adding other sources, and maybe it changes based on those sources, changing the conclusion of that sub-claim part of that argument; now the whole thing updates, and the conclusion might switch to 'maybe' or change from yes to no, whatever the point is.

The transparency in this process is crucial. Too many conversations about any topic become emotional because it's too difficult to keep all these things in our minds at once. A basic argument like just made here about recycling has multiple sub-claims in it and those individual sub-claims need to be backed by data, which is hard to do when we're trying to have a conversation.

Imagine where we could do this graphically or visually, showing the connections of how strong an individual claim is based on how much you trust an individual source. That's the power of this thing. And that's why I'm so excited about it; there are many more examples to follow!

Each of those objects in that diagram is another substrate component: claims, sources, they're all in there and inside of another repository inside of the Substrate project.

For instance, an example of a source might be New York Times, Associated Press, or Breitbart. When people make truth claims, it's important to fact-check or research those claims to see their support. Substrate does this by maintaining a list of those sources that we may or may not trust. The point is that some people will trust different sources and some won't; it depends on them.

Then the question becomes 'should you Ross the source,' which can make an argument itself. You might argue that they're putting too much weight onto a particular source, for instance. You could research those claims separately to discount that particular source whether it's the New York Times or Breitbart, or whatever it is.

When someone makes an argument or claim within an argument, it can be linked directly to those sources you do or don't trust. And when you look at this claim - 'inflation fell by 2% under this person's term,' the argument includes this claim with these sources: AP and New York Times. This shows the strength of the argument based on the source.

So, in conclusion, Substrate makes things that used to be almost impossible to discuss actually approachable and discussable because we can break it down into its individual pieces. Before, you might say 'you're just not able to counter all my arguments and evidence because I'm too smart.' But now, you could say 'look here's my argument; throw it up on the board.'

The Substrate project provides a visual representation of each component - claims, sources, and their connections, allowing for clearer and more transparent discussions about various topics.
Maybe it's like a little bit in the future, or you know, something similar to Apple Vision Pro, where everything becomes 3D. You could turn it around, like a piece of DNA, showing you claims you disagree with or sources that back up those claims. This allows for more logical and precise discussions.

This is just one example - the arguments example. Let's step back and think about real-world use cases for Substrate overall. It sounds really cool, but what does it actually do?

Keep in mind this is very early-stage; we've had multiple use cases since its release two days ago. 

The first use case involves describing oneself using AI art that represents connections between goals, missions, problems, solutions, and strategies. This visual representation can be seen through augmented reality glasses, making it easier to understand someone's identity.

Many people struggle with defining themselves. Substrate provides a versatile way to express one's self in text, audio, video, or even through AI conversations. Sharing your context allows others to see who you are easily. 

Another use case is visualizing oneself for organizations and individuals. For example, using Substrate to learn about someone's values, goals, projects, and progress can help build connections with like-minded people.

For personal relationships, Substrate could facilitate finding friends, mates, or business partners by matching on shared values, goals, beliefs, preferences, and interests.

In the next use case, Substrate is used for analyzing narratives, rumors, conspiracy theories, and viral claims. By using Substrate to break down arguments and claims, we can debunk misinformation effectively. For instance, a claim about never going to the moon contradicts the idea that it was faked by NASA, providing evidence against such conspiracy theories.

In conclusion, Substrate offers a variety of applications in personal identity expression, organization learning, and debunking misinformation. Its potential for fostering human connections is exciting.
All right, welcome to Unsupervised Learning. This is Daniel Miser, and today I'm super excited to announce a project I've been wanting to talk about for a very long time called Substrate.

Okay, let's get into the project itself. So, what is it exactly? What is Substrate?

Substrate is an open-source framework for human understanding, meaning, and progress. The purpose of this project is to make things that matter to humans more transparent, discussable, and ultimately because they're transparent and discussable, they'll be more fixable.

So, what kind of things are we talking about? We're calling these Substrate components, the components of human meaning right when we talk about understanding meaning and progress. These are the pieces that we're actually talking about:

1. Collections of ideas: A list of human novel ideas.
2. Problems: A list of our most important human problems.
3. Beliefs & Models: Our ways of conceptualizing reality, frames, a list of narratives or lenses for perceiving reality.
4. Solutions: A list corresponding to problems.
5. Information sources: New York Times, The Hill, Breitbart, lots of different sources of information, government sources, individual sources, different media organizations — comprehensive and spanning political ideologies.
6. Laws: All different legislation, starting with the US government but expanding out to pretty much the world at some point.
7. Claims: Factual claims or truth about the world.
8. Votes & Results: From laws that were submitted and voted on, saying here's what the votes were from different people, talking about Representatives voting on things.
9. Arguments: A list of arguments made in favor or against a particular thing.
10. Funding Sources: Lobbyists' agendas, missions, donations, goals.
11. Facts: Claims that have been verified and are important to note can become true and then untrue again.

Each component will be an actual list maintained in a repository within GitHub. We already have one of these:

[GitHub link](https://github.com/SubstrateOrg/SubstrateProjects)

This includes the problems component, which has a list of problems including:

1. Ransomware attacks on healthcare systems.
2. Teen depression in the UK.
3. Nuclear weapons development in North Korea.

Each item has a PR code for direct association and this is just the structure of each repository within the Substrate organization:
[Substrate Organization](https://github.com/SubstrateOrg)

When you go into repositories, you see that we've populated these components and there's already some pretty good activity on some of them, especially problems.

The structure allows the entire open-source community to contribute their own problems, claims, sources, frames, goals, etc., for all those different repositories which are all part of this Substrate component. I think you're starting to get it, but if not, one way to think about this is as a way to put handles onto things that are hard to discuss.

The whole reason I created this project is so that we can articulate things better to each other but also to ourselves.

Let's get into some actual examples here. So you can see what I'm talking about:

### Example: Argument Component

Think of a common argument we might hear on any given day about whatever topic. In this case, it's recycling:

- "I don't know why you recycle man, it's a total waste. It costs so much to recycle right now and the programs are poorly run."

This breaks down an argument into components like:
1. Effort required.
2. Cost of progress.
3. Limited results.

It helps us discuss arguments more clearly by breaking them down into digestible parts.
Then, it breaks those into further things regarding recycling programs, which require significant effort. Recycling programs are also expensive, and most rejected materials end up in landfills. Okay, okay.

And then it goes and adds research to all of those; in this case, it's pulled it directly out of the model but you can actually add AI on top of this. We're going to be doing with an agent framework either that we build ourselves or that we use one of the third parties, which will actually be tools doing this research down here.

Okay, going and doing separate lookups to find research like you could do this at really in-depth level for each stage here; especially, this one where you're doing the research. And then it comes back and says supports or weakens. Look at this:

- Supports
- Supports
- Weakens
- Weakens
- Partially supports

Then we have a conclusion that ends up being a weak argument interesting.

So, you could see the reasons this is the most important thing you could see how this argument was formed; how it was researched using what sources. Okay, look at this: 'Recycling statistics 2021', National Waste and Recycling Association (2022). So we actually have source names here, and we can go into even more depth if we do additional AI work on this.

And that's kind of a foreshadowing for the future section here. So let's just keep going again; what this does is it takes an argument like this recycling example and turns it into a graph like we just saw. 

The most important thing about this graph is that we could throw it up on a board, or we could throw it on the side of a wall, we could each view it inside of our AR glasses or whatever in the near future. Now both of us who are having this discussion can be looking at the same thing and saying 'uh', yeah I agree with these two but I don't agree with this one.

And the reason I don't agree is because I don't trust the source that it came from. And then you could do things like okay, let's grab some content from other sources; boom, you start adding other sources to it and maybe it changes based on those sources, it changes the conclusion of that subpart of that argument.

And now the whole thing updates, and the conclusion is maybe 'oh', we're not sure or maybe it switches it from yes to no or whatever the point is transparency. Okay, too many of our conversations about any topic can become emotional because it's too difficult to keep all these things in our minds at once.

A basic argument like was just made here about recycling has multiple subclaims in it, and those individual sub claims need to be backed by data. And it's very hard to do that just in our brains when they're we're in the middle of a conversation, especially if you're trying to 'like' blast this out.

You want to have this conversation; you want to say hey recycling is good or recycling is bad, or whatever the topic is but you try to put that on social media or somewhere. You're basically writing a text thing right which is trying to convince someone which is fine we've been doing that forever but imagine where we could do this graphically where we could do this visually and show the connections of how strong an individual claim is based on how much you trust an individual source, right?

So that's the power of this thing, and this is why I'm so excited about it. And there are many more examples we're about to get into. So each of those objects in that diagram is another substrate component; right, the claims, the sources they're all in there, and they're all in there inside of another repository inside of the substrate project.

So here's an example of a source: New York Times, Associated Press, Breitbart. When people make truth claims it's important to be able to fact check or research those claims to see their support. Substrate does this by maintaining a list of those sources that we may or may not trust; that's the point.

Some people will trust different sources some people will not trust them. And you can see the full argument and all of its support in one visual look at 'this claim': inflation fell by 2% under this particular person's term, right?

This argument includes this claim: this claim has this Source (the AP), this claim has this source New York Times, so this argument has a particular strength as a result of that. So argument to claims to sources, and this is why we're so excited about Substrate.

It's going to make things that used to be almost impossible to discuss actually approachable, actually discussable because we could break it down into its individual pieces. 

So before you'd be like 'you're just not able to counter all my arguments and evidence because I'm too smart', now you could say look here's my argument throw it up on the board.
Maybe it's like a little bit in the future, or you know, Apple Vision Pro or whatever, and now it's actually a 3D thing you could turn it around, like a piece of DNA or something. Right? Show me which claim you disagree with or which source you disagree with that backs up those claims right? So now we can just take this thing apart using different sources or whatever, and change the output. This will enable far more logical and precise discussions that that is what we're going for.

This is just one example - this is just the arguments' example, so now I want to take and like back up a little bit and think about real-world use cases for substrate overall.

Okay, sounds really cool, what do you actually do with it exactly? So this is my favorite: keep in mind this is very early. It literally came out like 2 days ago but we've already got multiple use cases for this thing okay so let's get into these okay?

The first one here is describing yourself. This one is massive look, look at this! This pretty cool art. From mid Journey it's a part of a design that I did for uh a previous piece, but anyway yeah, you could see these are meant to represent the different connections of like uh goals to Mission to problems that she thinks are most important in the world, Solutions she thinks uh are the answers to those problems, different strategies, different projects she's working on. That's what this uh AI art is meant to represent with this graph literal function here but then you can have labels assigned to that.

Keep in mind this is me looking at her in this coffee shop through my AR glasses and seeing okay, first of all purple is associated with engineering boom! She's an engineer. She's known for being a friend; she's known for being a writer so I'm now seeing this person as she is which she is previously defined.

So let's get into that many people have trouble describing who they are and what they are about. This is so critical with substrate - you can basically describe yourself in any way you want to right? Text, audio, video, whatever! Even have a conversation with AI which is not part of substrate yet but uh there's lots of different ways to do that and it will be able to both articulate and visualize you as a person. This is absolutely insane people have trouble describing who they are and what they're about this is going to help you do that, and if you share your context or your substrate representations with others, they'll be able to see what you're about.

They'll be able to see this! Okay, now of course the visuals here, the AR stuff I mean that's going to take some time. That's a separate project right? That's just visualization of data that's already there. Substrate is about creating that data for you - for organizations, for whatever in these individual components.

Learning a person's values, substrate will be a wonderful way to start learning about someone or something what they care about how they see the world, whatever! Imagine having something like this available when you're looking at someone or you're researching them?

Check this out we got a person here okay. Got this guy it's like the same coffee shop programmer gamer organizer and you've got this grid here right, or this graph here? Check this out: Mission merge gaming and programming continuous Learning Community Building innovation in Game Dev values goals projects annual pixel Jam AI NPC framework these are things that he's working on to further these particular projects and these are the goals that he's shooting for. For the mission of merging gaming and programming that's insane!

So now I know about this person, and if there's matches then I could walk up to them and be like hey, I hear you're into this or I, I he, hear you're into that. And now I have a conversation to start, or maybe my AI is having that conversation with his AI? Whatever depends how far in the future it is but this will be a wonderful way to learn about what somebody really cares about and how they see the world.

So check this out: they believe the most important problems are these three problems. This is really cool! And they believe the best Solutions are these solutions to those problems by NASA okay? And we have actions which is contradicted by leads to, and then we have another claim which is the red one. And then look at this provides attempts to explain demonstrate
Again, the actions or the verbs, then we have results. So, let's reflect: On the moon, consistently reflecting lasers back from Earth—this one, I didn't think of it; I dynamically created it just for the launch of the project. It was a great one! Okay, what about bouncing lasers off the moon if there aren't any reflectors on the moon? That would mean someone put them there, taking us into aliens—let's set that aside as a separate topic.

Multiple countries have independently verified moon landings; over 800 pounds of moon rocks have been studied worldwide. So you've got a collection of evidence that starts to add up. Conclusion: False. Overwhelming evidence supports moon landings. And this is just one level deep; we can go even deeper with sub-claims and supporting citations.

You might remember Snopes—a site for debunking or verifying rumors. This system works like Snopes but visually, allowing more transparency and individual validation of each component's validity. Any background can now evaluate this information with greater transparency than ever possible.

People could build their arguments using different sets of sources to see if the conclusions change. This is why we're excited about this particular argument piece. We've spent a lot of time on it because it's crucial—it has the potential to significantly strengthen our shared understanding of reality, allowing us to disagree in a far healthier way.

One claim: There's a tiny teapot orbiting the Sun. Investigated by space missions—data claims the teapot is too small for current instruments to detect. Result: No unusual objects detected; no evidence of a teapot found. Conclusion: False. Insufficient evidence supports the claim, just like with Snopes.

All this information adds up and compounds together. Now, let's discuss substrate and AI leading to actual action. This isn't about AI; it's about human meaning and progress. AI is simply a tool for helping that along.

Context sizes—prompting abilities—are increasing massively. Inference costs are falling dramatically. These things combined with Substrate's structured storage of information can work together beautifully, making the combination absolutely insane. We can feed goals (individuals, countries, cities, companies) into this system to untangle them, debate about them, vote on them, and then take action.

Some exciting examples for the combination of Substrate plus AI:
1. Automated hypothesis-to-results workflows in science: Science takes a long time because it's difficult to come up with ideas, design experiments, find funding, interpret results, publish them, and get them in front of influential people. With substrate, all these elements are stored together, allowing AI to help generate new ideas or hypotheses, design experiments, identify the best funding sources, collect funds, perform experiments, evaluate results, and disseminate findings effectively.

2. Funding requests: Once AI knows your goals and mission, it can suggest potential funding sources that would be most interested in supporting your objectives.

This integration of Substrate with AI paves the way for streamlined scientific progress, resource allocation, decision-making, and action-taking across various fields.
Maybe it knows how to contact them because that information is inside a substrate. Okay, so we can write the perfect pitch for you to get funding; help you set up experiments, and we're going to need some humans or robots to help with that part. But whatever running and monitoring the experiments, interpreting the results - all of this really right in the wheelhouse of AI. Writing the paper and sharing the paper also possible with AI, and getting better all the time. So, in other words, we're talking about hypothesis to proposed experiment, looking up funding sources, acquiring funding, running the experiment, publishing the results, making progress. In the beginning, this is still going to require a lot of human help, right? Especially at the idea and the running of the experiment phases, but over time AI will get better at that as well. But what we're talking about ultimately with this right here is the acceleration of science. Right because this cycle right here is leading to a whole bunch of failures and making us move on to do something else instead.

This whole pipeline, and I want to give credit to Joseph Ther for thinking about a very similar thing at a similar time like a year ago, talking about experiments and hypotheses and testing stuff like that. So, a lot of people probably thinking very similar things along these lines, but we are so excited about this idea of just being able to experiment and advance our knowledge forward through the most powerful mechanism that we're aware of which is science.

Accountability, okay? This one's insane - monitoring crime and corruption. The reason it's so easy to get away with corruption and crime right now is because there aren't enough people watching; gangs, cartels, embezzlers, dirty politicians. They're actually dropping evidence all the time - receipts, travel tickets, cameras, lots of different ways to know that a particular person was in a particular place.

It's not that they're being that careful because it's actually so difficult to go and collect that stuff and bring it together into a narrative. So usually, it takes a major journalist team or a massive law enforcement operation to dump thousands of hours of highly skilled work to collect all this different evidence. Then you have to do the analysis, then formulate the conclusions, document all of this, take it to the media - most crime and corruption slip by because nobody is simply watching; there aren't enough journalists, there aren't enough law enforcement teams who have the skills to do that stuff.

Substrate plus AI versus dirty politician. This is a use case: let's take substrate with some AI added on and think about a dirty politician taking massive gifts from a particular lobbyist.

Let's say this is some dirty Democrat or Republican - independent doesn't matter; it has nothing to do with that problem. It's there are so many donations, so many lobbyists, so many representatives, so many actual laws and bills, so many votes, but guess what? It's all public! We're talking about the US here; this is all public information.

It's required by law that all of this stuff is posted - the lobbyist groups must actually register themselves. The donations they make to any particular representative have to be public records. Meetings - I believe those are also public, and so are all the votes representatives make on bills where lobbyists have been donating and trying to influence. So a nonprofit or even just a project, a small project that comes out of Substrate or whatever, could use AI to collect all these different things continuously put them in substrate.

And they're already going in substrate because we're about to start dumping all the laws, all the different voting records, all the different histories for each lobbyist and also for each representative. All that goes right into substrate. To inspect; then AI can ingest all of that at any given moment, and basically tell us this: here are all the bills written by that person - here are all the summaries of those bills - basically what are they trying to do? Here's who those bills helped and who they hurt?

Right here are all the lobbyists that care about those particular issues. Here all the donations those groups made to that representative, or that particular representative, and here's how the representative voted on every single bill.

Then guess what? The AI is really good at this - it comes back with something like an assessment: this is a compromised politician. Reasoning ENT reveals: you can have ENT going and researching various things that this person is doing again all public all legal, right?

Talking about legal public documents reveal that he was legally gifted a small yacht last year which he tweeted about and later deleted. He's had 31 dinners in the last 18 months with them totaling over like almost $155,000.

ENT revealed that the lobbyist president used considerable influence
To get Bill Meyer's daughter admitted to an exclusive private school that she wasn't actually qualified for, every vote he's made about this particular issue has been in the direction that the lobbyist actually wants to happen. Previous votes before they started the relationship, the politician used to vote in the opposite direction. Therefore, the conclusion from this AI is: and by the way, you published the algorithm for the AI as well. We got another project called Fabric where you publish the actual thoughts and directions given to the AIS so that they're inspectable.

Right, you don't want people to think "oh, they came to that conclusion because it's bias." No, you can look and see the actual instructions given to the AI to evaluate this thing impartially. So now, you could trust this thing with a very high rate of confidence because you could see how it's thinking and you could see all the data sources just like before with arguments.

So basically, the incredibly important objects of legislation, votes, etc., are all things that can be monitored and collected and stored within Substrate so that's that one. Next one here: Leadership. This is absolutely abolutely powerful. Okay, I've been a consultant for a couple of decades now and I've worked with hundreds of startups, so many large corporations, and a big problem for most organizations, that includes governments, families, individuals, startups, corporations, everything is that they don't have Clarity. Just like a person, it's hard to know what they think the issues are, what they specifically plan on doing, and how they plan to measure progress.

So we see this with Business Leaders and we see this with politicians. So with Substrate, we intend to make it so that every leader will need to have a full detailed plan that has the following components: Imagine if everyone had this when they are pitching some plan for the high school or some plan to be a principal or some plan to be a community leader or some plan to be a politician, or whatever it is.

Here's what I think the problems are - remember this is a problem object inside of Substrate so you can actually look at them here's what I think the problems are. And coming off of the problem, here's what I think the solutions are. Here are my proposed strategies for accomplishing that. Here are the KPIs; these are the metrics. Here's how I'm actually going to measure myself, and how about this: fire me if I don't get the KPIs to this number by this date.

So at the end of the three and a half years when I'm going back up for reelection, I expect what whatever the thing is - the number of kids who don't go hungry in this High School, the literacy level in this High School, the unemployment rate, whatever it is - doesn't matter if I don't improve that number by X amount by this date. You have my permission to vote me out.

Imagine having that level of clarity and accountability for any leader trying to get any job doing anything. So really excited about that one okay, next one here: This is the best one okay I save the best for last. These are all adding on each other. Watch this look at this! I did a post a while back about how companies are essentially graphs of algorithms and I encourage you to go check that out.

I've got the link down here below but it's like "okay, you have a company that processes bad images come in they send them to you on the website and you then do a number of things to that photo. Right you do a high-quality scan, you repair it, you stylize it, you caption it, you send it to the user." Then there's a Marketing Group; a Marketing Group has an idea, it shares it with a team, they decide on the best version, they do this, they do a final vote, they do a launch campaign.

Okay or the uploading process, visit the website, create an account, click the upload link. These are all individual steps okay these are just algorithms and this is a graph of algorithms where they're all connected and you can break these into smaller and smaller pieces until you eventually see the world in this way. Okay I'm just going to say it like that: companies are just graphs of algorithms.

But think of it this way: I don't think I went far enough with that, everything can be conceptualized in this way, everything can be conceptualized in this way as a process. So essentially what you have is you have a current state of things right (state of the universe) but smaller down to a scale that we're currently at - which is companies and processes.
Dealing with a company, process, team, or department involves actions or events like decisions being made. These could be customer activities, purchasing items, insurance policy payouts, etc., which result in new states.

Incorporating human components such as jobs, decisions, strategies, lessons learned, conclusions, and reasons adds complexity. Humans' roles can connect these actions visually, linking all the elements into larger graphs to describe business or country operations comprehensively.

These graphs depict how decisions like "buy more stock" or "hire more people" impact a company or family dynamics. This visualization aids in understanding processes better, leading to improved operations and decision-making. The consulting industry is adapting, with 40% of companies focusing on AI consultation.

As AI technology improves, it will not only describe current states but also optimize them. Future and recommended states can be analyzed for mergers, hiring, process efficiency, and automation potential.

For families, corporations, churches, cities, or counties, this system provides a framework to analyze the impact of human actions on operations. More data enhances AI's ability to recommend improvements effectively.

In an example for a security team, collecting feedback revealed slow turnaround times were the primary concern. By adopting a flexible assessment model using fewer testers, 94% faster assessments were achieved, benefiting both security and engineering departments. This illustrates the process breakdown, visualization, and analysis that AI can provide for continuous optimization.
The right to summarize the world is hard to understand, and things that are hard to understand are hard to discuss and improve. The goal of Substrate is to address this problem by making the things humans care about more visible, discussable, and improvable. The framework is open-source and lives on GitHub.
At its core, it's a collection of crowd-sourced lists of the things humans care about and that make up our discourse in society. One major problem people in organizations have is not knowing or being able to communicate what they are about using this framework. People and organizations will be able to articulate their values and purpose more clearly which will not only help them but everyone that they interact with.
Substrate is magnified by AI because AI can (or soon will be able to) hold all of Substrate in its mind at once, from there we'll be able to ask all sorts of meaningful questions such as: What is this person or organization about? Are we pursuing the best path towards our goals? Or what are the most critical mistakes I'm currently making? Ultimately, this will allow us to take action on these things. For example: "What action should I do right now to optimize this workflow?" or "What should I do right now to achieve the best possible outcome that's aligned with my goals?"
In short, Substrate is a way to better understand and optimize the things we care about as humans, so we would love for you to get involved.
I want to give thanks to people who are already involved and are really into this: myself (Jonathan Dunn), Jason Had, Clint Gibler, Joseph Ther, Joel Parish, Robert Hansen, and some of the few that are already involved and excited about this. If you're interested please go to the Substrate project and let us know that you'd like to contribute.
Thank you for your time!
