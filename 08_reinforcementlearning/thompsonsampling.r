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

## Thompson sampling

# Initialising
ads_selected = seq(1,10)
num_rewards_1 = ds[1,]
num_rewards_0 = 1 - num_rewards_1

total_reward = sum(num_rewards_1)

# For each round, choose the ad with the maximum theta
for (n in 2:N) {
    ad = 1
    max_theta = 0
    
    for (i in 1:d) {
        theta = rbeta(1, num_rewards_1[[i]], num_rewards_0[[i]])

        if (theta > max_theta){
            ad = i
            max_theta = theta
        }
    }
    ads_selected = append(ads_selected,ad)
    reward = ds[n, ad]
    sum_rewards[ad] = sum_rewards[ad] + reward
    total_reward = total_reward +  reward
    
    if (reward == 1) {
        num_rewards_1[ad] = num_rewards_1[ad] + 1
    }
    else{
        num_rewards_0[ad] = num_rewards_0[ad] + 1
    }
}

# Visualising results
hist(ads_selected, 
     main = 'Histogram of ads selected',
     col = 'blue',
     xlab = 'Ads',
     ylab = 'Ad selection frequency density')