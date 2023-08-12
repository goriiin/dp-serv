package store

type Config struct {
	Database string `toml:"database_url"`
}

func NewConfig() *Config {
	return &Config{}
}
