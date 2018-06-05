# Reading in data

ds = read.csv('Ads_CTR.csv')

# Random sample

N = 10000
d = 10

random_reward = 0
for (n in 1:N) {
    ad = sample(1:d, 1)
    random_reward = total_reward + ds[n,ad]
}

## UCB algorithm

# Initialising
ads_selected = seq(1,10)
num_selections = rep(1,10)
sum_rewards = ds[1,]
total_reward = sum(sum_rewards)

# For each round, choose the ad with the maximum UCB
for (n in 2:N) {
    ad = 1
    max_upper_bound = 0
    
    for (i in 1:d) {
        rbar = sum_rewards[i]/num_selections[i]
        delta_i = sqrt(3/2 *log(n + 1)/num_selections[i])
        ucb = rbar + delta_i

        if (ucb > max_upper_bound){
            ad = i
            max_upper_bound = ucb
        }
    }
    ads_selected = append(ads_selected,ad)
    num_selections[ad] = num_selections[ad] + 1
    
    reward = ds[n, ad]
    sum_rewards[ad] = sum_rewards[ad] + reward
    total_reward = total_reward +  reward
}

# Visualising results
hist(ads_selected, 
     main = 'Histogram of ads selected',
     col = 'blue',
     xlab = 'Ads',
     ylab = 'Ad selection frequency density')