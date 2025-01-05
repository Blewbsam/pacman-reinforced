import torch
from PIL import Image
import torch.nn as nn
import numpy as np

class DQNAgent(nn.Module):
    def __init__(self,num_actions):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1),  # Reduce spatial dimensions
            nn.ReLU(),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=1, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(195, 512),  # Adjust based on input size and strides
            nn.ReLU(),
            nn.Linear(512, num_actions),  # Output layer for Q-values
        )
    def forward(self,x):
        return self.model(x)


class DQRNAgent(nn.Module):
    def __init__(self,num_actions):
        super().__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=16,kernel_size=3,stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32,out_channels=1,kernel_size=3,stride=1),
            nn.ReLU(),
            nn.Flatten()
        )
        self.lstm = nn.LSTM(input_size=195, hidden_size=512, batch_first=True)
        self.fc = nn.Linear(512, num_actions)  # Output 4 actions
    def forward(self, x):
        batch_size, seq_len, channels, height, width = x.size()

        x = x.view(batch_size * seq_len, channels, height, width)  # Shape: [batch_size * seq_len, channels, height, width]
        
        x = self.cnn(x)  # Shape: [batch_size * seq_len, feature_dim]
        
        feature_dim = x.size(-1)
        x = x.view(batch_size, seq_len, feature_dim)  # Shape: [batch_size, seq_len, feature_dim]
        
        # Process with LSTM
        lstm_out, (h_n, c_n) = self.lstm(x)  # LSTM output: [batch_size, seq_len, hidden_size]
        
        x = h_n[-1]  # Final hidden state: [batch_size, hidden_size]
        
        x = self.fc(x)  # Output shape: [batch_size, num_actions]
        return x
    

class DQRNDeepAgent(nn.Module):
    def __init__(self,num_actions):
        super().__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=16,kernel_size=3,stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32,out_channels=1,kernel_size=3,stride=1), # only different between two models
            nn.ReLU(),
            nn.Flatten()
        )
        self.lstm = nn.LSTM(input_size=195, hidden_size=512, num_layers=3,batch_first=True, dropout=0.2)
        self.fc = nn.Linear(512, num_actions)  
    def forward(self, x):
        batch_size, seq_len, channels, height, width = x.size()
        x = x.view(batch_size * seq_len, channels, height, width)  # Shape: [batch_size * seq_len, channels, height, width]
        
        x = self.cnn(x)  # Shape: [batch_size * seq_len, feature_dim]
        
        # Restore sequence dimension
        feature_dim = x.size(-1)
        x = x.view(batch_size, seq_len, feature_dim)  # Shape: [batch_size, seq_len, feature_dim]
        
        lstm_out, (h_n, c_n) = self.lstm(x)  # LSTM output: [batch_size, seq_len, hidden_size]
        

        x = h_n[-1]  # Final hidden state: [batch_size, hidden_size]
        
        # Fully connected layer for output
        x = self.fc(x)  # Output shape: [batch_size, num_actions]
        return x


v1 = DQRNAgent(4)
print(v1)
total_params = sum(p.numel() for p in v1.parameters())
print(total_params)

mode = DQRNDeepAgent(4)
print(mode)
total_params = sum(p.numel() for p in mode.parameters())
print(total_params)