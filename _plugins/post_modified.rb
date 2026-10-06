require 'open3'
require 'pathname'
require 'time'

# set blog metadata before archives, feeds, and sitemaps are generated
Jekyll::Hooks.register :site, :post_read do |site|
  site.posts.docs.each do |post|
    path = Pathname.new(post.path).relative_path_from(Pathname.new(site.source)).to_s
    modified = File.mtime(post.path).utc.iso8601

    begin
      changes, errors, status = Open3.capture3('git', '-C', site.source, 'status', '--porcelain', '--', path)

      # clean files use their last commit so checkout times do not change the timestamp
      if status.success? && changes.empty?
        timestamp, errors, status = Open3.capture3('git', '-C', site.source, 'log', '-1', '--follow', '--format=%cI', '--', path)
        modified = Time.iso8601(timestamp.strip).utc.iso8601 if status.success? && !timestamp.strip.empty?
      end
    rescue Errno::ENOENT
      # previews without git use the markdown file's modification time
    end

    post.data['modified'] = modified
    post.data['last_modified_at'] = modified
  end
end
