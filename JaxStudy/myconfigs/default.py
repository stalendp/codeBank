"""Default Hyperparameter configuration."""

import ml_collections


def get_config():
  """Get the default hyperparameter configuration."""
  config = ml_collections.ConfigDict()

  config.learning_rate = 0.1
  config.momentum = 0.9
  config.batch_size = 128
  config.num_epochs = 10
  return config
