# A sample Guardfile
# More info at https://github.com/guard/guard#readme

## Uncomment and set this to only include directories you want to watch
# directories %(app lib config test spec feature)

## Uncomment to clear the screen before every task
# clearing :on

guard 'livereload' do
  watch(%r{content_site/templates/simple_portfolio/.+\.(html|djhtml)$})
  watch(%r{content_site/static/simple_portfolio/js/.+\.(css|js)})
  watch(%r{content_site/static/simple_portfolio/css/.+\.(css|js)})
  # Rails Assets Pipeline
  watch(%r{(app|vendor)(/assets/\w+/(.+\.(css|js|html|png|jpg))).*}) { |m| "/assets/#{m[3]}" }
end
