from keras.models import load_model
import DJIA_sentiment_plus2 as djia
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

model = load_model('DJIA_model_plus2.h5')

#Political elections
news_aggregate_trump_election = ["The inauguration of Donald Trump: your guide to the events in Washington Palestine in the Age of Trump Donald Trump has assembled the worst Cabinet in American history Trump picks Sonny Perdue for agriculture secretary Roger Cohen On Trumps Russia Challenge How Trumps Trade Advisers Are Planning To Shake Up China Trump Renews Vow for Jerusalem Embassy, a Gift of Uncertain Value Memo To Steven Mnuchin: Trumps Tax Plan Would Add $7 Trillion To The Debt Over 10 Years Trumps treasury secretary pick failed to disclose nearly $100m in assets Trump's Washington Hotel Draws Protesters — And Ethics Concerns What to Expect in Donald Trump's First 100 Days The America Donald Trump Is Inheriting, By The Numbers Trump: My Cabinet has highest IQ of any Cabinet ever assembled Donald Trump inauguration: President-elect to be sworn into office with Abraham Lincolns Bible Trump team prepares dramatic cuts What Trumps Proposed Spending Cuts Could Mean for the Arts Economy Trumps Foreign Policy Philosophy Hard to Pin Down Conflict of interest fear as Trump looks to expand Scotland golf resort Trumps unexpected impact on markets in seven charts Trump Sought Military Equipment For Inauguration, Granted 20-Plane Flyover Trumps Team Said to Be Planning to Privatize Public Broadcasting Trump’s anti-immigration stance could result in a $60 billion food shortage Seriously? Schools reportedly to black out Trumps inaugural address Trump wants to lead America — with a Cabinet that doesnt look anything like it Trump has already delivered: Glenn Reynolds"]
news_aggregate_macron = ["Emmanuel Macron vows unity after winning French presidential election Five reasons why Macron won the French election How Emmanuel Macron went from top of the class to president of France Emmanuel Macron’s unlikely path to the French presidency Emmanuel Macron Wins Pivotal French Presidential Election Macron beats Le Pen to win French presidency, toughest tasks to come Macron needs to build a parliamentary majority to help fulfill his campaign promises For Labour MPs desperate to return British politics to the centre, Macron's victory is a beacon Emmanuel Macron's irresistible charm US far-right activists, WikiLeaks and bots help amplify Macron leaks: Researchers Why Macron's victory is reassuring ... and yet not Macron campaign office vandalized with anti-Semitic graffiti Fear of Le Pen drives many French in Ireland to Macron What Macron Can Do for Free Markets Everywhere Team Macron: a mix of youthful energy and wise heads Macron has shown grit and guile, but can he go the distance? Macron: The youngest ever French president How Macron, the boy who preferred the company of adults, became president of France Emmanuel Macron set to be President of France Macron's Victory ‘Vive la France’: Emmanuel Macron celebrates victory in French capital Emmanuel Macron Beats Marine Le Pen and Twitter Totally Rips President Trump Emmanuel Macron 'loves to take holidays in Britain' but will still aim to destroy Brexit Massive crowd celebrates macron win in Paris World reacts as Emmanuel Macron, 39, becomes France's youngest president"]
news_aggregate_italian_election = ["Italy election: Populist Five Star and League vie for power Italy's voters choose populists, deliver stinging rebuke to Europe Italy anti-establishment parties make big gains in election In Italy Election, Anti-E.U. Views Pay Off for Far Right and Populists What's next for Italy? The post-election scenarios Eurosceptic Italy in race to form majority government The Guardian view on Italian elections: a lesson for progressives Italy's stock market slides after uncertain election result 4 Takeaways From a ‘Throw the Bums Out’ Italian Election Europe ends on a high note despite Italy's political uncertainty; AXA sinks 9.7% As populists surge, Italy heads for political impasse Matteo Salvini: far-right leader steps out of Berlusconi's shadow Mattarella stuck in quagmire over creation of Italy’s government Make no mistake – right-wing populism is making a resurgence in Europe, as the Italian elections show Italy Takes a Step Back From Europe AS IT HAPPENED: Uncertainty ahead as Italy election results come in Demagogues Win as Europe’s Populist Tide Sweeps Italy Italian banks, bonds bear brunt of election fallout Steve Bannon: Election was Italy’s version of Trump vote Italy Blames Europe, Sparking Populist Rise ECB chief Draghi tells wife to 'shut up' as she dismisses chances of him being Italy PM Italy's Election Was Quite Traditional, Actually Promised Revolution Italians May End Up With Little Change On Energy, Italy's Five Star Movement Could Rock The Boat Italy's frightening elections Result"]
news_aggregate_german_election = ["Merkel Re-Elected as Right Wing Enters Parliament Germany’s election results in charts and maps German elections 2017: Angela Merkel wins fourth term but AfD makes gains – as it happened What to watch in Germany’s election German elections: Far-right wins MPs for first time in half a century Jews around world alarmed by far-right breakthrough in Germany Jews Cast Wary Eye on German Election Results, With Strong Showing of Far-Right AfD Party Real-time tracking system measures Russian interference in German elections Merkel wins, nationalist breakthrough France's Le Pen congratulates German far-right AfD The troubling German election results prove that far-right nationalism is by no means dead in Europe Exit polls offer Merkel fewer coalition choices Clinton Says Angela Merkel Is The Most Important Leader In The Free World Facts and figures about Germany as the country goes to the polls Mixed-member proportional and the 2017 election Far right rises in the east in German general election How Germany chooses its chancellor The Global Leadership Vacuum German Voting Day: Sights of the Bundestag Election 2017 German vote could doom Merkel-Macron deal on Europe German voters deal a blow to Macron’s EU reform drive German Federal Election Results How to understand Germany’s new political landscape Le Pen, Wilders salute German hard right advance Rabbis praise Merkel after reelection: 'A responsible leader'"]
news_aggregate_midterms = ["Midterm elections 2018: When are the next US elections? Follow the Nov. 6 midterm election live with up-to-the-minute results Full Replay: President Trump Responds To 2018 Midterms; Time To Put Partisanship Aside Midterm results open door to more oversight of President Trump Midterm elections 2018 results: Who won the midterms? Who won Senate and House? Florida midterm elections 2018 results: Who won midterm elections in Florida? Election results: Bill Nelson presses forward with recount in Florida Senate race World reacts to U.S. midterm elections Trump Declares Midterm Results A 'Tremendous Success'. Here's Why He's Wrong Midterm election results: Taylor Swift-endorsed Democrat fails to win Tennessee Senate seat What Does the Outcome of the Midterm Elections Mean for Medicaid Expansion? President Trump calls media 'hostile,' says of CNN reporter Jim Acosta: 'You are a rude, terrible person' Four ways the internet changed the midterm elections Facebook May Have Passed Midterms Test, But Still Has Lots of Work to Do A Fraught Congressional Election Comes to a Close in California Donald Trump suffers a midterms setback, US stocks come back down to earth. Where do investors go next? Pot Stocks Surge on Heels of Midterm Election Results FULL RESULTS: Recount Expected in Senate Race; DeSantis Wins Florida Gov. US midterms fallout: Trump fires Sessions, vows to fight Democrats if probes into administration launched Read the Resignation Letter Attorney General Jeff Sessions Submitted to President Trump Daily Briefing: Europe and markets ponder U.S. midterm mixed bag JPMorgan's Kolanovic Says Midterms May Make Trump Drop Trade War Biotech Stocks and the Midterm Elections Midterm Results Leave Canadians Wary Over Fate of Trade Agreement Minitrue: No Unauthorized Reports on U.S. Midterms"]
#Trump decisions
news_aggregate_kim = ["Read the full text of the Trump-Kim agreement here The most bizarre moments from the Kim-Trump summit Donald Trump, Kim Jong-un pledge peace and security at Singapore summit but doubt surrounds denuclearisation pact Read: full text of Trump-Kim agreement Trump, Kim vow to denuclearize North Korea Five talking points from the historic Kim-Trump talks The Latest: Trump Thanks Kim for Taking 'Bold Step' ‘World will see a major change:’ Kim, Trump sign declaration Here’s what body language experts are saying about the Trump-Kim meeting Trump really has achieved a historic breakthrough – for the Kim dynasty North Korean starvation and killings? Trump says Kim Jong Un is 'very talented' but not 'nice' Donald Trump and Kim Jong Un sign the blandest of agreements Kim Jong Un Committed To Denuclearisation, Says Trump After Historic Summit 'Now the real work begins:' Experts weigh in on Trump-Kim nuclear pledge Trump Kim summit: Six odd moments from the day Trump makes a deal with Kim – but what exactly is it? Democrats accuse Trump of doing ‘anaemic’ deal with Kim North Korean state media hails Kim-Trump summit success From G-7 to Kim summit, 'a bad week for American strength around the world' The Sensational Idiocy of Donald Trump’s Propaganda Video for Kim Jong Un Trump-Kim summit: Leaders sign 'comprehensive' document; Kim says world will see major change Highlights: Donald Trump and Kim Jong Un's historic summit A Successful Trump-Kim Summit Could Be the Prelude to War With Iran Trudeau vs. Kim: Trump calls Canadian PM ‘weak’ and North Korean dictator ‘talented’ TRUMP SPENDS NORTH KOREA DEBRIEF OBSESSING OVER JUSTIN TRUDEAU"]
news_aggregate_tariff = ["President Trump Signs Tariff Order on Metals With Wiggle Room for Allies Trump shows steely resolve ahead of tariff announcement U.S. Steel: Major Winner From Proposed 25% Tariff On Steel The looming global trade war Trump tariffs: US President imposes levy on steel and aluminium Why U.S. Steel Stocks Aren't Loving Tariffs Trump sets steel and aluminum tariffs but exempts Canada, Mexico The five no-good arguments for tariffs Trump’s most hardcore America First trade adviser is on the brink of getting a lot more power What Investors Need To Know About The Implications Of Trump's Tariffs Canada spared from President Trump's tariffs, 'for now' European Central Bank: Trump Tariff Move 'Dangerous' ECB Draghi: Unilateral Tariffs Are 'Dangerous', But We're Not In a Trade War Yet White House: Adjusting Imports of Steel Into the United States Donald Trump could REMOVE tariffs from selected countries as China joins backlash No Trade War Yet With U.S. Due To Planned Tariffs, German Minister Says Canada and 10 other nations sign TPP as Trump plans U.S. tariffs Is Canadian steel and aluminum actually a security risk to U.S.? Steel and aluminum tariffs to begin in 15 days, says AP Overnight Finance: Trump signs tariffs, defying GOP | Republicans look to narrow tariffs | Vote on Dodd-Frank rollback pushed to next week | Trump says Cohn could return to WH Oil falls with U.S. output climb pushing prices to a more than 3-week low Elon Musk tweets at Trump to vent about how China taxes U.S. vehicles – and Trump quotes him in announcing new steel tariff while touting a proposed 'reciprocal tax' Musk asks Trump for equal, fair car import tariffs Trump signs order for tariffs to take effect this month Trump: Tariffs are a necessity for national security"]
news_aggregate_climate = ["Obama Emissions Rules Could Yield $300 Billion Annually by 2030 Trump: Another Nixon? As the climate continues to change, Al Gore’s here to boil down the science Someone Just Noticed That Trump Is Getting Stuff Done A Dim Outlook for Trumponomics ESG INVESTING   Trump Touts 'Clean Coal,' But His Policies Don't Support It Trump’s Generals Are Trying to Save the World. Starting With the White House. Dear Liberals, Ivanka Trump Was Never Your Ally Schwarzenegger unveils initiative to tweak Trump on climate Schwarzenegger launches new effort to counter Trump on climate Al Gore says An Inconvenient Sequel is hopeful in face of Donald Trump Al Gore on Miami’s future, new sequel to his climate movie and Donald Trump Paris Agreement Trump admin leaves room to stay in pact Trump administration delivers notive US intends to withdraw from Paris climate deal U.S. submits formal notice of withdrawal from Paris climate pact Trump and the Paris Agreement: What Just Happened? Donald Trump: Washington formally tells UN of Paris agreement withdrawal Trump’s ‘inverse Midas touch’ Free advice for the next journalist who gets an interview with President Trump The Top Five Foreign-Policy Blunders Trump Hasn’t Made Yet Fact check: Trump overstates impact of immigration bill National security adviser attempts to reconcile Trump’s competing impulses on Afghanistan An Inconvenient Sequel: The Al Gore Documentary And The Donald Trump Election Report: The World Invested $264 Billion in New Renewables in 2016"]
news_aggregate_tax = ["Donald Trump signs $1.5 trillion tax bill into law Remarks by President Trump at Signing of H.R. 1, Tax Cuts and Jobs Bill Act, and H.R. 1370 President signs tax overhaul into law Tax Cuts to Cost $1 Trillion After Growth, Official Study Finds Much-Feared Tax Bill Pays Dividends for Tech Workers What The GOP's Final Pass-Through Tax Cut Means For Business Owners With Cuomo Assist, Homeowners Rush to Soften Tax Bill’s Impact President Trump Signs New Income Tax Law into Effect - New Brackets and Deductions for 2018 Commentary: Real Estate Investors Will Love This Last-Minute Change to the Tax Plan What changes in the 2018 Tax Cuts and Jobs Act? Here's a short course Your Guide to Capital Gains Taxes in 2018 What They Are Saying About Effects of Trump Tax Cuts on Insurance Industry Estate & gift tax changes under 2017 tax cut and jobs act Four Things Educators Should Know About the Tax Bill Trump Just Signed Trump's tax bill and regulatory reform will spark an economic boom, benefitting all Americans Trump ends year in character – dodging questions and singing his own praises Trump signs GOP tax plan and short-term government funding bill on his way out of town Trump should make vulnerable Democrats who opposed his tax cuts pay the price in 2018 Donald Trump signs Tax Cuts Act into law Trump Signs $1.5 Trillion Tax Cut in First Major Legislative Win GE Cash Crunch That Hit Dividend May Get Worse Under Trump Tax Cuts Corporate America's tax-cut generosity: Is it real? Trump claims Kraft praised the tax plan and pledged to open a new factory What Will The Tax Bill Do To Birth Control? It Could Be Major Credit Suisse expects to take £1.7bn writedown after Trump tax reforms"]
news_aggregate_shutdown = ["Asked Who ‘Gets Fired’ In An Obama Shutdown, Trump Told Fox News: The President Trump learned nothing from the midterms. Exhibit A: the shutdown. Federal Shutdown Compounds Risks for US Economy  How Trump’s government shutdown affects the average American Locked doors, cancelled tours: US national parks suffer amid shutdown Government officially enters partial shutdown as Congress misses funding deadline The Government Partially Shut Down at Midnight. Here's What That Means America’s government shuts down, once again US government partially shuts down over border wall row US government shutdown appears set to continue until Thursday as fight over Trump's border wall stalls spending talks Parts of US gov't shut down after politicians fail to reach deal The Government Shut Down Over Trump’s Border Wall. What Happens Next? Trump cancels Mar-a-Lago Christmas trip over shutdown U.S. government shutdown continues with no indication Trump, Democrats near deal Donald Trump warns of 'long stay' amid partial government shutdown over Mexico wall US government shutdown: Billions for border wall will 'never' pass Senate vote, Democrats tell Trump Trump says he's working with Democrats during the partial government shutdown, but his border security meeting only included Republicans The government shutdown means no paid vacation for federal workers Shutdown over border wall and other recent Trump decisions aimed at placating his base The government shutdown, in photos N.J. House Democrats use same word to describe government shutdown under Trump: tantrum A Trump-approved government shutdown is a fitting end to Paul Ryan's disappointing, hypocritical tenure Who Is Paid During A Government Shutdown? Here's Who Will & Won't Be Affected Trump Will See Shutdown Affect His Approval, Disapproval Ratings Trump appears to sign blank ‘bill’ before shutdown"]
#Others
news_aggregate_zuckerberg = ["Mark Zuckerberg faces tough questions in two-day congressional testimony – as it happened Congress doesn’t know how Facebook works and other things we learned from Mark Zuckerberg’s testimony Mr. Zuckerberg Goes To Washington: The Climb Up To Capitol Hill 7 takeaways from Mark Zuckerberg’s appearance before the House Mark Zuckerberg was ready to slam Apple if Congress asked him about Tim Cook's privacy comments Mark Zuckerberg was ready to take on Apple and Tim Cook Conservative lawmakers had a question for Mark Zuckerberg: What about Diamond and Silk? Republican lawmakers go after Facebook CEO Zuckerberg for anti-conservative bias Who are Diamond and Silk and why is everyone talking about them? Mark Zuckerberg Is Deluded If He Thinks AI Can Solve Facebook’s Hate Speech Problem Mark Zuckerberg Just Revealed the Biggest Flaw on Social Media. Hint: It's Not the Data Leaks Zuckerberg Vows to Step Up Facebook Effort to Block Hate Speech in Myanmar Five clueless questions United States senators asked Mark Zuckerberg “SENATOR, I THINK WE ALREADY DO”: ZUCKERBERG’S INTERROGATION TURNS INTO TECH SUPPORT Mark Zuckerberg’s Hearing Proves You Know More About Facebook Than Most Senators Mark Zuckerberg Used a Booster Seat in Congress and Twitter Had a Field Day Jimmy Kimmel Edits Mark Zuckerberg's Testimony With Even Better Questions From Senators Jimmy Kimmel taunts Mark Zuckerberg after testifying in 'big boy clothes' Watch ‘Mark Zuckerberg’ Field Senator Selfie Questions on ‘Kimmel’ Sen. Ted Cruz Makes Mark Zuckerberg Look Sympathetic on Capitol Hill Hey, Mark Zuckerberg. Who Have You Texted Today? Where did you stay last night?: How US Senate mocked Mark Zuckerberg on privacy The best reactions and memes from Mark Zuckerberg’s congressional testimony Black members of Congress criticize Zuckerberg: Facebook “does not reflect America” GOP Rep. Bob Latta Weighs In On Second Day Of Zuckerberg's Testimony"]
news_aggregate_harvey_hurricane = ["Harvey Weakens Over Louisiana As Houston Copes With Record Rainfall Scientists Explain Why Harvey Was So Devastating Why has Harvey's rain been so extreme? How Harvey Will Change Texas Katrina. Sandy. Harley. The debate over the climate and hurricanesis getting louder and louder Hurricane Harvey pushes gas prices near two-year high On the heels of Hurricane Harvey, Tropical Storm Irma forms; U.S. impact unknown Texas pastor Joel Osteen: Backlash over not opening megachurch for shelter 'probably helped us to step up some things' Sandra Bullock donates $1 million for Harvey relief These companies are donating $1 million or more to Harvey relief efforts Red Cross Exec Doesn't Know What Portion Of Donations Go To Harvey Relief Trump Killed Obama’s Flood Protection Rule Two Weeks Ago Opinion: Harvey’s ravaging of Houston is perfect reason to kill the flood insurance program Hurricane Harvey Energy Crisis Could Be Nightmare For U.S. Economy Harvey shuts down largest US oil refinery, bears down on Louisiana plants Flash Floods Hit Beaumont and Port Arthur, Texas, After Harvey Makes Landfall Port Arthur Faces Harvey Flooding Disaster: ‘Our Whole City Is Underwater’ With Its Economic Heft, Houston Is Equipped to Recover From Harvey Just like Katrina, black Americans will be hit hardest by Hurricane Harvey Texan man who lost six family members to Harvey recounts moment they were swept away in flood How to avoid Hurricane Harvey charity scams and make sure your money gets to victims who need help Meet the Man Who Turned His Furniture Stores Into Shelters for Harvey Victims How Schoolchildren Will Cope With Hurricane Harvey Hurricane Harvey: Leonardo DiCaprio, Sandra Bullock Give $1 Million Each Harvey kills 15 Houston police officers"]
news_aggregate_apple_1_trillion = ["Apple becomes world's first trillion-dollar company Apple becomes first US-listed trillion-dollar company How Tim Cook and the iPhone made Apple America's first $1 trillion company Apple Becomes First Trillion-Dollar Public Company Apple Is Worth One Trillion Dollars Apple becomes first U.S. company to reach $1 trillion market cap Apple is the first trillion dollar company: What was the first billion dollar valuation? Apple now worth $1 trillion thanks to tax cuts and tax aversion schemes Big record! Apple becomes first US company to hit $1 trillion in market cap Apple just hit a $1 trillion market cap—here's why its little-known third co-founder sold his 10% stake for $800 Apple’s $1 Trillion Milestone Reflects Rise of Powerful Megacompanies Apple Just Hit $1 Trillion. Here's How Rich You'd Be If You Bought Stock at These 5 Key Moments Apple’s romp to $1 trillion market cap helps S&P 500, Nasdaq notch gains Apple's stock may wear the trillion-dollar crown, but IBM held more sway over the stock market in its heyday Oops! Apple's Own Stock Tracking App Wrongly Claims It As World's first trillion dollar company 4 Comparisons Between Aramco And Apple, Two Trillion-Dollar Companies Apple gets its ultimate revenge on Michael Dell with the world’s first trillion-dollar market cap Apple makes history as the iPhone maker becomes the world's first trillion dollar company Apple's Stock Surge May Just Have Made Warren Buffett's Berkshire Hathaway $2.6 Billion Richer Apple May Be the First Trillion-Dollar Company, but Can You Believe the 2001 Brendan Fraser Film Monkeybone Isn’t on Netflix?? Asian shares cautious amid elevated US-China trade tensions Opinion: Why Apple’s trillion-dollar market cap is nothing to celebrate Apple becomes first trillion-dollar company Apple reaches $1 trillion market capitalisation Apple reached $1 trillion. These companies aren’t far behind"]
news_aggregate_italian_government_formed = ["The Eurocrisis Is Back And It Could Be Uglier Than The Last One Italy Ain't Over Till the Bond Vigilantes Sing Judy Asks: Is Italy the Achilles Heel of Europe? Italy needs to be handled with care Italy's game of euro chicken What Italy’s crisis means for Europe Italy crisis poses dilemma for Draghi over ECB’s next step Italy’s President Asks Populists: Call Me When You’re Ready Italy to have first populist government as Giuseppe Conte asked to be prime minister again Italy’s political turmoil could mark the end of the EU, roiling global markets Italy’s political crisis is roiling financial markets once more Italy’s president approves populist Rome government Italy political crisis: Populist government gets a second chance Trade wars, China, Italy: Future shock is here, and here to stay Houlihan Lokey's Gold Says He's Troubled by Italy's Political Crisis Italy turmoil accelerates outflows from Europe Spinning Italy's Distressed Debt Into Gold Amid Italy's political crisis, Europe braces for a no-confidence vote against Spain's prime minister 'The Troika would have to march into Rome': German MEP says Brussels could take control of Italy's finance ministry if populist parties form a Eurosceptic government Decline and fall? How Italy fell out of love with the euro Italy buys back €500m of its debt amid political woes As Italy forms anti-establishment government, row erupts with EU Juncker: Italians need to work harder and be less corrupt Italy crisis dents Greek hopes of returning to bond markets Italy, Who Wins? The Market, the Euro or Voters?"]

# Choose the news aggregate that you prefer for example, midterms?
news_aggregate = news_aggregate_shutdown

#vectorizing the news from whch we want to have a signal by the pre-fitted tokenizer instance
news_aggregate = djia.tokenizer.texts_to_sequences(news_aggregate)
#padding the string to have exactly the same shape as the model input
news_aggregate = pad_sequences(news_aggregate, maxlen=djia.max_sequence_length, dtype='object')
#print(news_aggregate)
sentiment = model.predict(news_aggregate,batch_size=1,verbose = 2)[0]
if(np.argmax(sentiment) == 0):
    print("Bearish sentiment")
elif (np.argmax(sentiment) == 1):
    print("Bullish sentiment")